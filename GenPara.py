def paraCheck(openB,closeB,n,s=[]):
	if closeB==n:
		print(''.join(s))
		return
	else:
		if(openB>closeB):
			s.append(')')
			paraCheck(openB,closeB+1,n,s)
			s.pop()
		if openB<n:
			s.append('(')
			paraCheck(openB+1,closeB,n,s)
			s.pop()
		return

paraCheck(0,0,3)