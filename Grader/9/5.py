class TeamStats:
	def __init__(self, name, wins, loss, draws, scored, conceded):
		self.__name	= name
		self.__wins	= wins
		self.__loss	= loss
		self.__draws	= draws
		self.__scored	= scored
		self.__conceded	= conceded
		self.__total_point	= self.set_point()
		self.__goal_dif		= self.__scored - self.__conceded
  
	def get_name(self)	: return self.__name
	def get_point(self)	: return self.__total_point
	def get_gd(self)	: return self.__goal_dif
 
	def set_point(self)	: return  (3*self.__wins + self.__draws)

class SortAlgorithm:
	def special_insertion_sort(teamlst):
		def	_compare(team1 : TeamStats, team2 : TeamStats):
			if team1.get_point() > team2.get_point():
				return True
			elif team1.get_point() == team2.get_point():
				return team1.get_gd() > team2.get_gd()
			else:
				return False
		
		for i in range(1, len(teamlst)):
			key = teamlst[i]
			j = i - 1
			while j >= 0 and not _compare(teamlst[j], key):
				teamlst[j + 1] = teamlst[j]
				j -= 1
			teamlst[j + 1] = key


class Solution:
	def main(self):
		raw_teams_stats = input('Enter Input : ').split('/')
        
		teams_lst = []
		for team in raw_teams_stats:
			name, wins, loss, draws, scored, conceded = team.split(',')
			teams_lst.append(TeamStats(name,int(wins),int(loss),int(draws),int(scored),int(conceded)))
  
		SortAlgorithm.special_insertion_sort(teams_lst)
  
		print("== results ==")
		for t in teams_lst:
			print([t.get_name(), {"points": t.get_point()}, {"gd": t.get_gd()}])
   

sol = Solution()
sol.main()