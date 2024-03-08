nums = [1, 2, 3]

print(type(nums))

# lista pode add numeros repetidos

nums.append(3)
nums.append(3)
nums.append(4)

print(len(nums))

nums[3] = 190

nums.insert(0,-200)

# para pegar o ultimo elemento é só pegar a posição -1
print(f'{nums[-1]} - ultimo elemento da lista')

print(nums)