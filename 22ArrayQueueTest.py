from ArrayQueue import ArrayQueue
def main():
	q = ArrayQueue(25)
	print(q.isEmpty())
	print(q.size())
	q.insert(20)
	print(q.size())
	q.insert(50)
	print(q.size())
	q.insert(10)
	print(q.size())
	print(q.isEmpty())
	print(q.size())
	print(q.remove())
	print(q.remove())
	print(q.remove())
	q.insert(50)
	q.insert(10)
	print(q.size())
	print(q.remove())
	print(q.remove())
	#print(q.remove())
	print(q.isEmpty())

main()

