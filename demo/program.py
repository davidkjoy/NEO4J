from py2neo import Graph
graph = Graph("bolt://localhost:7687", auth=("neo4j", "graph"))




def create_patient():

    allergies = {}
    medication = {}
    
    print("Enter patient id: ")
    id = int (input())
    print("Enter patient name: ")
    name = input()
    print("Enter Year of Birth: ")
    yob = int(input())
    print("Enter city: ")
    city = input()
    
    print("Does patient has allergies (y/n): ")
    alrgy_choice = input()
    alrgy_count = 0
    while (alrgy_choice == 'y'):
        alrgy_count += 1
        print("Enter allergy: ")
        allergy = input()
        allergies[str('allergy_') + str(alrgy_count)] = str(allergy)
        print("Does patient has  another allergies (y/n): ")
        alrgy_choice = input()
    
    query = 'CREATE (' + name.replace(" ","_") + ':patient{id: ' + str(id) + ', name: "' + name + '", YOB: ' + str(yob) + ', City: "' + city + '"}) '
    
    alrgy_query = ''
    
    
    graph.run(query)
    
    
 
def return_all_nodes():
    data = graph.run("MATCH(n) RETURN n").to_table()
    print(data)

create_patient()
return_all_nodes()