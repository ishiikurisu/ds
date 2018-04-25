import consultant

if __name__ == '__main__':
    flag = True
    flow = consultant.get_flow_by_name('')
    if flow is not None:
        flag = False
        print('Finding something that doesnt exist')

    flow = consultant.get_flow_by_name('Susanne Rath')
    if len(flow) != 19:
        flag = False
        print('invalid flow')

    if flag:
        print('ok')
