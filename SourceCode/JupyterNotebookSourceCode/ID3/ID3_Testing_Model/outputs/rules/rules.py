# ID3
def findDecision(obj): #obj[0]: How.far.do.you.commute.to.school., obj[1]: Do.you.have.experience.with.online.classes., obj[2]: Do.you.have.easy.access.to.the.internet., obj[3]: Are.you.the.owner.of.the.computer.you.use.for.school., obj[4]: Do.you.easily.get.distracted.at.home., obj[5]: Are.you.taking.a.lab., obj[6]: In.general..do.you.prefer.labs.online.or.in.person..
	# {"feature": "In.general..do.you.prefer.labs.online.or.in.person..", "instances": 30, "metric_value": 0.9871, "depth": 1}
	if obj[6] == 'In-person':
		# {"feature": "How.far.do.you.commute.to.school.", "instances": 24, "metric_value": 0.8709, "depth": 2}
		if obj[0] == '0-20 miles':
			# {"feature": "Are.you.taking.a.lab.", "instances": 10, "metric_value": 0.8813, "depth": 3}
			if obj[5] == 'Yes':
				# {"feature": "Do.you.easily.get.distracted.at.home.", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[4] == 'No':
					# {"feature": "Do.you.have.experience.with.online.classes.", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1] == 'Yes':
						# {"feature": "Do.you.have.easy.access.to.the.internet.", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2] == 'Yes':
							# {"feature": "Are.you.the.owner.of.the.computer.you.use.for.school.", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[3] == 'Yes':
								return 'In-person'
							else: return 'In-person'
						else: return 'In-person'
					else: return 'In-person'
				elif obj[4] == 'Yes':
					return 'In-person'
				else: return 'In-person'
			elif obj[5] == 'No':
				# {"feature": "Do.you.have.experience.with.online.classes.", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[1] == 'Yes':
					# {"feature": "Do.you.have.easy.access.to.the.internet.", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[2] == 'Yes':
						# {"feature": "Are.you.the.owner.of.the.computer.you.use.for.school.", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[3] == 'Yes':
							# {"feature": "Do.you.easily.get.distracted.at.home.", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[4] == 'Yes':
								return 'Online'
							else: return 'Online'
						else: return 'Online'
					else: return 'Online'
				else: return 'Online'
			else: return 'In-person'
		elif obj[0] == '20-40 miles':
			# {"feature": "Do.you.have.experience.with.online.classes.", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[1] == 'Yes':
				# {"feature": "Do.you.easily.get.distracted.at.home.", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[4] == 'Yes':
					# {"feature": "Are.you.taking.a.lab.", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[5] == 'Yes':
						# {"feature": "Do.you.have.easy.access.to.the.internet.", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[2] == 'Yes':
							# {"feature": "Are.you.the.owner.of.the.computer.you.use.for.school.", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[3] == 'Yes':
								return 'In-person'
							else: return 'In-person'
						else: return 'In-person'
					elif obj[5] == 'No':
						return 'In-person'
					else: return 'In-person'
				elif obj[4] == 'No':
					# {"feature": "Are.you.taking.a.lab.", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[5] == 'Yes':
						return 'In-person'
					elif obj[5] == 'No':
						return 'Online'
					else: return 'Online'
				else: return 'In-person'
			elif obj[1] == 'No':
				return 'Online'
			else: return 'Online'
		elif obj[0] == '40-60 miles':
			return 'In-person'
		else: return 'In-person'
	elif obj[6] == 'Online':
		return 'Online'
	else: return 'Online'
