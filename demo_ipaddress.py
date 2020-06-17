
import binascii
import ipaddress

def test1():
	ADDRESS = [
	    '10.9.0.6',
	    'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa',
	]

	for ip in ADDRESS:
		addr = ipaddress.ip_address(ip)
		print(addr)
		print('{!r}'.format(addr))
		print('   IP version:', addr.version)
		print('   is private:', addr.is_private)
		print('  packed form:', binascii.hexlify(addr.packed))
		print('      integer:', int(addr))
		print()

def  is_ip_Valid(ipaddr):
	try:
	    ipaddress.ip_address(ipaddr);
	    return True;
	except :
	    return False;

def test2():
	NETWORKS = [
	    '10.9.0.0/24',
	    'fdfd:87b5:b475:5e3e::/64',
	]

	for n in NETWORKS:
	    net = ipaddress.ip_network(n)
	    print('{!r}'.format(net))
	    print('     is private:', net.is_private)
	    print('      broadcast:', net.broadcast_address)
	    print('     compressed:', net.compressed)
	    print('   with netmask:', net.with_netmask)
	    print('  with hostmask:', net.with_hostmask)
	    print('  num addresses:', net.num_addresses)
	    print()

def test3():
	NETWORKS = [
    '10.9.0.0/24',
    'fdfd:87b5:b475:5e3e::/64',
	]

	for n in NETWORKS:
	    net = ipaddress.ip_network(n)
	    print('{!r}'.format(net))
	    for i, ip in zip(range(3), net):
	        print(ip)
	    print()

def test4():
	NETWORKS = [
	    '10.9.0.0/24',
	    'fdfd:87b5:b475:5e3e::/64',
	]

	for n in NETWORKS:
	    net = ipaddress.ip_network(n)
	    print('{!r}'.format(net))
	    for i, ip in zip(range(3), net.hosts()):
	        print(ip)
	    print()

def test5():
	NETWORKS = [
	    ipaddress.ip_network('10.9.0.0/24'),
	    ipaddress.ip_network('fdfd:87b5:b475:5e3e::/64'),
	]

	ADDRESSES = [
	    ipaddress.ip_address('10.9.0.6'),
	    ipaddress.ip_address('10.7.0.31'),
	    ipaddress.ip_address('fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa'),
	    ipaddress.ip_address('fe80::3840:c439:b25e:63b0'),
	]


	for ip in ADDRESSES:
	    for net in NETWORKS:
	        if ip in net:
	            print('{}\nis on {}'.format(ip, net))
	            break
	    else:
	        print('{}\nis not on a known network'.format(ip))
	    print()

def test6():
	ADDRESSES = [
	    '10.9.0.6/24',
	    'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa/64',
	]

	for ip in ADDRESSES:
	    iface = ipaddress.ip_interface(ip)
	    print('{!r}'.format(iface))
	    print('network:\n  ', iface.network)
	    print('ip:\n  ', iface.ip)
	    print('IP with prefixlen:\n  ', iface.with_prefixlen)
	    print('netmask:\n  ', iface.with_netmask)
	    print('hostmask:\n  ', iface.with_hostmask)
	    print()

if __name__ == "__main__":
	# test1()
	# print(is_ip_Valid('2001:db8::'))
	# print(is_ip_Valid('192.168.168.1'))
	# test2()
	# test3()
	# test4()
	# test5()
	test6()