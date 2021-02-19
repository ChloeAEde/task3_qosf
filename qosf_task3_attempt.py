###QOSF Task 3 attempt by Chloe Allen-Ede###
##This code still needs devlopment but I am rather proud with what I have so far :)

import numpy as np

#defining our qubits
global zero, one
zero=np.array([[1],[0]]) #ket(0)
one=np.array([[0],[1]]) #ket(1)

#identitiy matrix 
global identity
identity=np.eye(2)


#def multipleq(*args):
def multipleq(args):
    #creates how many qubit states as input/*args
    qubits=np.array([[1]])
    for i in args:
        qubits=np.kron(qubits, i)
    return qubits

def normalise(state):
    #normalisation function
    norm=state/np.linalg.norm(state)
    return norm

def x_gate(*args):
    #function to return the x gate
    X=np.array([
    [0,1],
    [1,0]
    ])
    #result=np.dot(X,args)
    return X

def Hadamard(target, n, u):
    #function that gives the hadamard gate
    H=(1/np.sqrt(2))*np.array([
        [1,1],
        [1,-1]
    ])
    
    return H


def CNOT(target,no_q,size):
    p0=np.dot(zero,zero.T)#projector
    p1=np.dot(one,one.T)
    control=target[0]
    target=target[1]

    X=x_gate()
    
    if control==0:
        Cnot=multipleq(getIdentities(p0, size)) + multipleq(getIdentities(p1, size, target, X))
    
    else:
        Cnot=multipleq(getIdentities(p1, size)) + multipleq(getIdentities(p0, size, target, X))
    while(no_q.shape != Cnot.shape):
        no_q=np.kron(no_q,identity)
    newstate=np.dot(Cnot, no_q)
    return newstate

def getIdentities(pWhat, num, Xpos=-1, X=-1):
    temparr = [pWhat]
    count = 1
    while(count < num):
        if(count == Xpos):
            temparr.append(X)
        else:
            temparr.append(identity)
        count += 1
    return temparr



def user():
    print("|0> is definded as zero \n|1> is defined as one")
    print("Change the my_circuit variable and the my_q variable")


user()
my_circuit = [
{ "gate": "h", "target": [0] }, 
{ "gate": "cx", "target": [0, 1] }
]

my_q=[one,zero,one,zero,one]#|01010>
size=len(my_q)

no_q=multipleq(my_q)


functions = {"h": Hadamard, "cx": CNOT, "X": x_gate}
for item in my_circuit:
    gate = item["gate"]
    target = item["target"]

    output=functions[gate](target, no_q, size)
    no_q = output
    
print("Here is the vector output", no_q)