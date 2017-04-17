from threading import Lock
from cStringIO import StringIO

import pandas as pd
import matplotlib; matplotlib.use('SVG')
from matplotlib import pyplot as plt
from flask import Flask, Response, request
from flask import render_template


app = Flask(__name__)
app.debug = True
mpl_lock = Lock()


@app.route('/')
def get_index():
    return render_template('index.html', server_data='Hello')


@app.route('/graph.svg', methods=['POST'])
def svg_from_csv():
    try:
        df = pd.read_csv(request.files['file'])
        with mpl_lock:
            df.plot(
                title='Plot',
                figsize=(8, 5))
            sio = StringIO()
            plt.savefig(sio)
            svg_data = sio.getvalue()
    except Exception as err:
        svg_data = 'Data error: {}'.format(err)
    return render_template(
        'graph.html',
        svg_data=svg_data,
        name=request.files['file'].filename)
    return Response(svg_data, 200)


@app.route('/graph.csv', methods=['POST'])
def csv_from_csv():
    try:
        df = pd.read_csv(request.files['file'])
        csv_data = df.head().to_csv()
    except Exception as err:
        csv_data = 'Data error: {}'.format(err)
    return Response(csv_data, 200, {'Content-Disposition': 'attachment;filename=test.csv'})


if __name__ == '__main__':
    app.run()
