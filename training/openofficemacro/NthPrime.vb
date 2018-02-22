REM  *****  BASIC  *****

Sub Main

End Sub

Function IsPrime(x)
	Dim flag as Boolean
	Dim i as Integer

	i = 2
	flag = True
	Do While i < x
		If (x Mod i) = 0 Then
			flag = False
		End If
		i = i + 1
	Loop

	IsPrime = flag
End Function

Function NthPrime(n)
	Dim result as Integer
	Dim counter as Integer

	result = 0
	If n >= 1 Then
		result = 1
		counter = 0
		Do While counter < n
			result = result + 1
			If IsPrime(result) Then
				counter = counter + 1
			End If
		Loop
	End If

	NthPrime = result
End Function
