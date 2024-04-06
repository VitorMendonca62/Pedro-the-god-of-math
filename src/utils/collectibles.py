from classes.Collectible import symbols_collectibles 

def analyze_victory(collected_dict): # collected_dict refere-se ao dicionário dos coletáveis coletados e o collectibles refere-se ao dicionários da quantidade de coletáveis
  count = 0
  for key in symbols_collectibles.keys():
    if collected_dict[key] == symbols_collectibles[key]:
      count += 1 
  
  return count == 4