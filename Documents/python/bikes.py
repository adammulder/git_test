bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)


motorcycle = []
motorcycle.append('honda')
motorcycle.append('yamaha')
motorcycle.append('suzuki')
motorcycle.append('ducati')

print(motorcycle)

too_expensive = "ducati"
motorcycle.remove(too_expensive)
print(motorcycle)
print("\nA " + too_expensive.title() + " is too expensive for me.")
