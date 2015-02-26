def check_connection(network, first, second):
    net = list(network)
    for x in net:
        if first in x:
            if second in x:
                return True
            else:
                net.remove(x)
                new = x.replace(first, '').replace('-', '')
                return check_connection(net,new,second)
    return False​
