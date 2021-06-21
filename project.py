# ÁREA DE DADOS

queues     = []  
idx_queues = {}

def print_all_queues():
    for queue in queues:
        print(f"\nFILA DE ATENDIMENTO PARA O DIA {queue['name']}")
        print(f"CONSULTAS NO DIA: ({queue['qtd']}/{queue['max']})")
        print(queue['queue'])

def add_queue(dic_queue):
    idx_queues[dic_queue['name']] = len(queues)
    queues.append(dic_queue)

def add_element(queue_name, element):
    if queues[idx_queues[queue_name]]['qtd'] >= queues[idx_queues[queue_name]]['max']:
        print("\nNão foi possível agendar a consulta de {} para o dia {}. Tente outra data." .format(element, queue_name))
    else:
        print("Consulta de {} agendada com sucesso para o dia {}! Será o {}º paciente a ser atendido." .format(element, queue_name, queues[idx_queues[queue_name]]['qtd'] + 1))
        queues[idx_queues[queue_name]]['queue'].append(element)
        queues[idx_queues[queue_name]]['qtd'] += 1

def remove_element(queue_name):
    if queues[idx_queues[queue_name]]['qtd'] > 0:
        queues[idx_queues[queue_name]]['queue'].pop(0)
        queues[idx_queues[queue_name]]['qtd'] -= 1

# ÁREA DE POC

add_queue({
    'name': '02/08/2021',
    'max': 5,
    'qtd': 0,
    'queue': []
})

# Agendamento de consulta de 5 pessoas para o dia 02/08

add_element('02/08/2021', 'Maria')
add_element('02/08/2021', 'Marta')
add_element('02/08/2021', 'João')
add_element('02/08/2021', 'Joaquim')
add_element('02/08/2021', 'Fernando')

print_all_queues()

# Tentativa falha de agendar consulta para mais uma pessoa no dia 02/08 e o programa retornará uma mensagem de erro
add_element('02/08/2021', 'Paula')

# Retirar a pessoa da fila de atendimento após ter sido atendida

remove_element('02/08/2021')
remove_element('02/08/2021')

print_all_queues()
