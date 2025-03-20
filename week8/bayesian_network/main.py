from week8.bayesian_network.node import Node

def main():
    # nodes
    cold_weather_node = Node("Cold Weather")
    lack_of_sleep_node = Node("Lack of Sleep")
    getting_sick_node = Node("Getting Sick")

    # edges
    getting_sick_node.add_parent(cold_weather_node)
    getting_sick_node.add_parent(lack_of_sleep_node)

if __name__ == '__main__':
    main()