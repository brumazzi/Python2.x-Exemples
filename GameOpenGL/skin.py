import loadmodel as lm

class skin():

	__slots__ = 'health','mana','stamin','attack','defense','agilit','luck','magic','magic_attack','magic_defense','critical_damage','critical_change','weapon','armor','cap','boots','belt','necklace','glove','cape','runa_1','runa_2','cristal','classe','element','job_1','job_2','abilits','tecnics','model'

	def __init__(self):
		self.health = .0
		self.mana = .0
		self.stamin = .0
		self.attack = .0
		self.defense = .0
		self.agilit = .0
		self.luck = .0
		self.magic = .0
		self.magic_attack = .0
		self.magic_defense = .0
		self.critical_damage = .0
		self.critical_change = .0
		self.weapon = None
		self.armor = None
		self.cap = None
		self.boots = None
		self.belt = None
		self.necklace = None
		self.glove = None
		self.cape = None
		self.runa_1 = None
		self.runa_2 = None
		self.cristal = None
		self.classe = None
		self.element = None
		self.job_1 = None
		self.job_2 = None
		self.abilits = None
		self.tecnics = None
		self.pos = []
		self.status = []
		self.vital = []
		for i in range(0,3):
			self.pos.append(float(.0))
			self.vital.append(.0)
		for i in range(0,5):
			self.status.append(.0)
		self.model = lm.BRZZ()

	def _refresh(self):
		#################################################################
		##                          ATTACK                             ##
		#################################################################

		self.status[0] = self.attack
		if self.classe:
			self.status[0] += self.classe.damage*1.387

		if self.weapon:
			self.status[0] += (self.weapon.damage)*0.03
		if self.armor:
			self.status[0] += (self.armor.damage)*0.03
		if self.cap:
			self.status[0] += (self.cap.damage)*0.03
		if self.boots:
			self.status[0] += (self.boots.damage)*0.03
		if self.belt:
			self.status[0] += (self.belt.damage)*0.03
		if self.necklace:
			self.status[0] += (self.necklace.damage)*0.03
		if self.glove:
			self.status[0] += (self.glove.damage)*0.03
		if self.cape:
			self.status[0] += (self.cape.damage)*0.03
		if self.runa_1:
			self.status[0] += (self.runa_1.damage)*0.03
		if self.runa_2:
			self.status[0] += (self.runa_2.damage)*0.03
		if self.cristal:
			self.status[0] += (self.cristal.damage)*0.03

		#################################################################
		##                          DEFENSE                            ##
		#################################################################

		self.status[1] = self.defense
		if self.classe:
			self.status[1] += self.classe.resist*1.387
		
		if self.armor:
			self.status[1] += (self.armor.resist)*0.03
		if self.weapon:
			self.status[1] += (self.weapon.resist)*0.03
		if self.cap:
			self.status[1] += (self.cap.resist)*0.03
		if self.boots:
			self.status[1] += (self.boots.resist)*0.03
		if self.belt:
			self.status[1] += (self.belt.resist)*0.03
		if self.necklace:
			self.status[1] += (self.necklace.resist)*0.03
		if self.glove:
			self.status[1] += (self.glove.resist)*0.03
		if self.cape:
			self.status[1] += (self.cape.resist)*0.03
		if self.runa_1:
			self.status[1] += (self.runa_1.resist)*0.03
		if self.runa_2:
			self.status[1] += (self.runa_2.resist)*0.03
		if self.cristal:
			self.status[1] += (self.cristal.resist)*0.03

		#################################################################
		##                          AGILIT                             ##
		#################################################################

		self.status[2] = self.agilit
		if self.classe:
			self.status[2] += self.classe.speed*0.896

		if self.weapon:
			self.status[2] += (self.weapon.speed)*0.03
		if self.armor:
			self.status[2] += (self.armor.speed)*0.03
		if self.cap:
			self.status[2] += (self.cap.speed)*0.03
		if self.boots:
			self.status[2] += (self.boots.speed)*0.03
		if self.belt:
			self.status[2] += (self.belt.speed)*0.03
		if self.necklace:
			self.status[2] += (self.necklace.speed)*0.03
		if self.glove:
			self.status[2] += (self.glove.speed)*0.03
		if self.cape:
			self.status[2] += (self.cape.speed)*0.03
		if self.runa_1:
			self.status[2] += (self.runa_1.speed)*0.03
		if self.runa_2:
			self.status[2] += (self.runa_2.speed)*0.03
		if self.cristal:
			self.status[2] += (self.cristal.speed)*0.03

		#################################################################
		##                         LUCK                                ##
		#################################################################

		self.status[3] = self.luck
		if self.classe:
			self.status[3] += self.classe.luck*0.017

		if self.weapon:
			self.status[3] += (self.weapon.luck)*0.03
		if self.armor:
			self.status[3] += (self.armor.luck)*0.03
		if self.cap:
			self.status[3] += (self.cap.luck)*0.03
		if self.boots:
			self.status[3] += (self.boots.luck)*0.03
		if self.belt:
			self.status[3] += (self.belt.luck)*0.03
		if self.necklace:
			self.status[3] += (self.necklace.luck)*0.03
		if self.glove:
			self.status[3] += (self.glove.luck)*0.03
		if self.cape:
			self.status[3] += (self.cape.luck)*0.03
		if self.runa_1:
			self.status[3] += (self.runa_1.luck)*0.03
		if self.runa_2:
			self.status[3] += (self.runa_2.luck)*0.03
		if self.cristal:
			self.status[3] += (self.cristal.luck)*0.03

		#################################################################
		##                       MAGIC                                 ##
		#################################################################

		self.status[4] = self.magic
		if self.classe:
			self.status[4] += self.classe.magic*1.387

		if self.weapon:
			self.status[4] += (self.weapon.magic)*0.03
		if self.armor:
			self.status[4] += (self.armor.magic)*0.03
		if self.cap:
			self.status[4] += (self.cap.magic)*0.03
		if self.boots:
			self.status[4] += (self.boots.magic)*0.03
		if self.belt:
			self.status[4] += (self.belt.magic)*0.03
		if self.necklace:
			self.status[4] += (self.necklace.magic)*0.03
		if self.glove:
			self.status[4] += (self.glove.magic)*0.03
		if self.cape:
			self.status[4] += (self.cape.magic)*0.03
		if self.runa_1:
			self.status[4] += (self.runa_1.magic)*0.03
		if self.runa_2:
			self.status[4] += (self.runa_2.magic)*0.03
		if self.cristal:
			self.status[4] += (self.cristal.magic)*0.03

		#################################################################

		self.magic_attack = self.status[4]*0.19 + self.classe.magic * 0.18
		self.magic_resist = self.status[4]*0.19 + self.classe.magic * 0.11

		self.critical_damage = self.attack * 2
		self.critical_change = self.classe.c_change
