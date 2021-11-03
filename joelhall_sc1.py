from mininet.topo import Topo

class MyTopo(Topo):

	def build(self):
		h9 = self.addHost('h9', ip='10.0.1.1/24')
		h10 = self.addHost('h10', ip='10.0.2.1/24')
		s9 = self.addSwitch('s9')
		self.addLink(h9,s9)
		self.addLink(h10,s9)

		s10 = self.addSwitch('s10')
		s13 = self.addSwitch('s13')
		self.addLink(s9,s10, bw ='10')
		self.addLink(s9,s13)

		s11 = self.addSwitch('s11')
		s12 = self.addSwitch('s12')
		self.addLink(s10,s11)
		self.addLink(s10,s12, bw ='15', delay='10ms')

		h1 = self.addHost('h1', ip='10.0.1.10/24')
		h2 = self.addHost('h2', ip='10.0.1.11/24')
		self.addLink(s11, h1)
		self.addLink(s11,h2)

		h3 = self.addHost('h3', ip='10.0.1.12/24')
		h4 = self.addHost('h4', ip = '10.0.1.13/24')
		self.addLink(s12,h3)
		self.addLink(s12,h4)

		s14 = self.addSwitch('s14')
		s15 = self.addSwitch('s15')
		self.addLink(s13, s14, bw='20', delay='5ms')
		self.addLink(s13,s15)

		h5 = self.addHost('h5', ip='10.0.2.10/24')
		h6 = self.addHost('h6', ip='10.0.2.11/24')
		self.addLink(s14,h5)
		self.addLink(s14,h6)

		h7 = self.addHost('h7', ip='10.0.2.12/24')
		h8 = self.addHost('h8', ip='10.0.2.13/24')
		self.addLink(s15,h7)
		self.addLink(s15,h8)

topos = {'mytopo': ( lambda: MyTopo()) }
