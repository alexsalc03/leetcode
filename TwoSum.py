EASY


#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order

num = input("inserisci elementi array separati da uno spazio: ")
num = list(map(int, num.split()))
target = int(input("inserisci il numero target: "))

print(f"input: nums: {num}, target: {target}")

def trova_indici (array,numero):
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[i] + num [j] == target:
               return (i,j)
    return None

risultato = trova_indici(num,target)

if risultato:
    print (f"[{risultato}]")
else:
    print("no combination found")

#explanation: i iterate two times on the array , using the second time to sum every
#combination and check if was equal to the target
