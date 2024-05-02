import statsapi

# statsLeaders = statsapi.get('stats_leaders', {'leaderCategories':'hits', 'statType':'statsSingleSeason'
#                                        ,'season':"2024"})
#
# print(statsLeaders)

season = statsapi.get('season', {'sportId':'1', 'seasonId':"2024"})

print(season)