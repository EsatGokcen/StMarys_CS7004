from week8.bayesian_network.node import Node

def main():
    # nodes
    cold_weather_node = Node("Cold Weather")
    lack_of_sleep_node = Node("Lack of Sleep")
    getting_sick_node = Node("Getting Sick")

    # edges
    getting_sick_node.add_parent(cold_weather_node)
    getting_sick_node.add_parent(lack_of_sleep_node)

    # probabilities
    cold_weather_node.cpt.update({(True, ) : 0.3})
    cold_weather_node.cpt.update({(False, ) : 0.7})

    lack_of_sleep_node.cpt.update({(True, ) : 0.4})
    lack_of_sleep_node.cpt.update({(False, ) : 0.6})

    getting_sick_node.cpt.update({(True, True) : 0.6})
    getting_sick_node.cpt.update({(True, False): 0.4})
    getting_sick_node.cpt.update({(False, True): 0.3})
    getting_sick_node.cpt.update({(False, False): 0.1})

if __name__ == '__main__':
    main()