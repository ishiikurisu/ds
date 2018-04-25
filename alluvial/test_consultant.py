import consultant
import sys

if __name__ == '__main__':
    consultant.setup(sys.argv[1])
    flag = True

    flow = consultant.get_flow_by_name('')
    if flow is not None:
        flag = False
        print('Finding something that doesnt exist')

    flow = consultant.get_flow_by_name('Susanne Rath')
    if len(flow) != 19:
        flag = False
        print('invalid flow')

    flow = consultant.get_flow_by_name('João Sarkis Yunes')
    if len(flow) != 19:
        flag = False
        print('invalid flow for yunes boi')
    else:
        print('yunes here: {0}'.format(', '.join(flow)))

    cv_file = consultant.get_cv_by_name('Lee Luan Ling')
    if cv_file is not None:
        flag = False
        print('How did you find it?')

    cv_file = consultant.get_cv_by_name('João Sarkis Yunes')
    if cv_file is None:
        flag = False
        print('There should be a XML file here, right?')
    else:
        print('Are you sure {0} is {1} CV?'.format(cv_file, 'João Sarkis Yunes'))

    if flag:
        print('ok')
