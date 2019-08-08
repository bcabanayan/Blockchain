import hashlib
import requests

import sys


# TODO: Implement functionality to search for a proof 

def proof_of_work(last_proof):
    """
    Simple Proof of Work Algorithm
    Find a number p such that hash(last_block_string, p) contains 6 leading
    zeroes
    """
    proof = 0
    # for block 1, hash(1, p) = 000000x
    # find value for proof that, when hashed with last block string, generates value with 6 leading 0s
    # guess and check until you find the answer you need
    print('Starting work on a new proof...')
    while valid_proof(last_proof, proof) is False:
        proof+= 1
    print('Sending to server...')
    return proof

def valid_proof(last_proof, proof):
    """
    Validates the Proof:  Does hash(block_string, proof) contain 6
    leading zeroes?
    """
    # build string to hash()
    guess = f'{last_proof}{proof}'.encode()
    # use hash function
    guess_hash = hashlib.sha256(guess).hexdigest()
    # check if there are 6 leading 0s in hash result
    beg = guess_hash[0:6] #[:6]
    if beg == "000000":
        return True
    else:
        return False

if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    coins_mined = 0
    # Run forever until interrupted
    while True:
        # TODO: Get the last proof from the server and look for a new one
        
        # TODO: Generate request with /last_proof

        # Look for a new one
        new_proof = proof_of_work(last_proof)
        
        # When found, POST it to the server {"proof": new_proof}
        # We're going to have to research how to do a POST in Python
        # HINT: Research `requests` and remember we're sending our data as JSON
        
        data = {'proof': new_proof}
        
        # sending post request and saving response in object

        r = requests.post(url = node+'/mine', data = data)
        
        # TODO: If the server responds with 'New Block Forged'
        # add 1 to the number of coins mined (for THIS client) and print it.  Otherwise,
        # print the message from the server.
        if r.message == 'New Block Forged':
            coins_mined += 1
            print(r.message + ', coins mined: ' + str(coins_mined))
        else:
            print(r.message)
        
