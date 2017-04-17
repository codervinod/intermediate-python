"""Commands dealing with optimization."""
import json
import time
import logging
from contextlib import contextmanager

import boto3
import requests

log = logging.getLogger(__name__)
sqs = boto3.resource('sqs')


class Queue(object):

    def __init__(self, url):
        self._url = url

    def recv_message(self):
        raise NotImplementedError()

    def send_message(self, msg):
        raise NotImplementedError()

    def delete_message(self, msg_id):
        raise NotImplementedError()

    @classmethod
    def create(cls, url, sqs=False):
        if sqs:
            return SQSQ(url)
        else:
            return SSQ(url)

    @contextmanager
    def retiring_message(self):
        msg_id, msg = self.recv_message()
        try:
            yield msg
        except Exception:
            raise
        else:
            self.delete_message(msg_id)

    def reactor(self, handle_message, raise_exceptions=True):
        while True:
            try:
                with self.retiring_message() as msg:
                    handle_message(msg)
            except Exception as err:
                if raise_exceptions:
                    raise
                log.error('Error processing message: %s', err)


class SSQ(Queue):
    """Super-simple Queue."""

    def recv_message(self):
        while True:
            res = requests.get(self._url)
            if res.status_code == 404:
                time.sleep(1)
                continue
            res.raise_for_status()
            return None, res.json()

    def send_message(self, msg):
        message_data = json.dumps(msg)
        res = requests.put(
            self._url,
            data=message_data,
            headers={'Content-Type': 'application/json'})
        res.raise_for_status()

    def delete_message(self, msg_id):
        log.info(
            'Would delete %s, were such functionality to be meaningful',
            msg_id)


class SQSQ(Queue):
    """AWS SQS Queue."""

    def __init__(self, url):
        super(SQSQ, self).__init__(url)
        self._queue = sqs.Queue(url)

    def recv_message(self):
        while True:
            msgs = self._queue.receive_messages(
                MaxNumberOfMessages=1,
                VisibilityTimeout=60 * 60,
                WaitTimeSeconds=20)
            if msgs:
                msg = msgs[0]
                return msg, json.loads(msg.body)

    def send_message(self, msg):
        message_data = json.dumps(msg)
        self._queue.send_message(
            MessageBody=message_data)

    def delete_message(self, msg_id):
        msg_id.delete()
