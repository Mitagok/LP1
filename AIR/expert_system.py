class ExpertSystem():

	def __init__(self):
		self.source = 'symtomps'
		self.SymtompsDict = {}
		self.SymtompToDisease = {}
	def read(self):
		reader = open(self.source, 'r')

		for line in reader:
			tokens = line.split(',')
			filtered_tokens = []
			disease_name = tokens[0].strip()[1:-1]
			#print("Disease name: " + disease_name)
			
			n = len(tokens)
			for i in range(1,n):
				curr = tokens[i].strip()
				filtered_tokens.append(curr)
				try:	
					self.SymtompToDisease[curr].append(disease_name)
				except KeyError:
					self.SymtompToDisease[curr] = list()
					self.SymtompToDisease[curr].append(disease_name)
				#print(curr, end = ",")
			#print()
			self.SymtompsDict[disease_name] = filtered_tokens

	def detect(self):
		#print(str(self.SymtompToDisease))
		#print("\n\n\n"+ str(self.SymtompsDict))
		symtomps = input('Enter the symtomps, seperated by comma: ')
		tokens = symtomps.split(',')
		
		filtered_tokens = []
		for token in tokens:
			filtered_tokens.append(token.strip().lower())

		print(filtered_tokens)
		for ft in filtered_tokens:
			try:
				disease_names = self.SymtompToDisease[ft]
				visited = set()
				for disease_name in disease_names:
					if disease_name in visited:
						continue					
					disease_symtomps = self.SymtompsDict[disease_name]
					self.calculate_probablity(disease_name,disease_symtomps,filtered_tokens)
					visited.add(disease_name)
			except KeyError:
				print('Unable to find disease for symtomp: ' + ft)
				continue
		
	def calculate_probablity(self, disease_name,disease_symtomps, user_input):
		n = len(disease_symtomps)
		count = 0		
		for symtomp in user_input:
			if symtomp in disease_symtomps:
				count = count+1
		print("Probablity that disease is: " + disease_name + " = " + str(count/n))

expert_system = ExpertSystem()
expert_system.read()
expert_system.detect()
