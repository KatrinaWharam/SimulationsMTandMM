import os
import numpy as np

params = {
    'number_of_motors': 100,
    'l1': '4',
    'l2': '4',
    'n2': '0.5878 0.8090 0'
}

def get_params(dx):
    l1 = float(params['l1'])
    dl = np.arange(-l1/2,l1/2+0.001,dx)
    parameterList = []
    for xpos in dl:
        for ypos in dl:
            new_params = params.copy()
            new_params['x2'] = f'{xpos} {ypos} 0.05'
            parameterList.append(new_params)
    return parameterList

def run(dx):
    parameterList= get_params(dx)
    if not os.path.isdir('configFiles'):
        os.system('mkdir configFiles')
    if not os.path.isdir('fiberPos'):
        os.system('mkdir fiberPos')
    if not os.path.isdir('coupleState'):
        os.system('mkdir coupleState')
    for parameters in parameterList:
        name  = 'pos__'+parameters['x2'].replace(" ", "_")+'_n2__' +parameters['n2'].replace(" ", "_")
        os.system('cp config.cym '+ name + '.cym')
        file = open(name + '.cym', "a")
        file.write(
            'new 1 microtubule \n'
            '{\n'
            '   length= ' + parameters["l1"]+' \n'
            '   direction = 1 0 0\n'
            '   position = 0 0 0 \n'
            '}\n'
            f'new {parameters["number_of_motors"]} motor\n'                          
            'new 1 microtubule \n'
            '{\n'
            '   length=' +parameters["l2"]+'\n'
            '   direction=' +parameters["n2"]+'\n'
            '   position =' +parameters["x2"]+'\n'
            '}\n'
            'new event \n'
            '{\n '
            '   delay = 0.2\n '
            '   code = report fiber '+'fibers_'+name+'.txt\n'
            '}\n'
            'new event \n'
            '{\n '
            '   delay = 0.2\n '
            '   code = report couple:state '+'couples_'+name+'.txt\n'
            '}\n'                                       
            'run 10000 simul system\n'
            '{\n '
            '   nb_frames=0 \n'
            '}\n'
        )
        file.close()
        os.system('./sim '+name + '.cym')
        os.system('mv ' + name + '.cym' + ' configFiles')
        os.system('mv ' + 'fibers_'+name+'.txt' + ' fiberPos')
        os.system('mv ' + 'couples_'+name+'.txt' + ' coupleState')

run(0.5)
