def myfunction():
    import ipdb; ipdb.set_trace();
    print 'I am here'


def otherfunction():
    print 'Now here'
    myfunction()

def main():
    otherfunction()
    print 'Now done'
    print 'exiting'

if __name__ == '__main__':
    main()