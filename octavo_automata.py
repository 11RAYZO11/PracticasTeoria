#palabra = raw_input("ingresa la cadena:  ") + ";"

#n1 = ""
#n2 = ""
#o =""

i = 1
while i > 0:
	
	palabra = raw_input("ingresa la cadena:  ") + ";"
	if palabra == ";":
		break
	n1 = ""
	n2 = ""
	o = ""
	estado = "q0"
	for entrada in palabra:
		if estado == "q0":
			if entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" or entrada=="0":
				estado = "q1"
			    	n1 += entrada
		    	if entrada == "*" or entrada == "+" or entrada == "-" or entrada == "/" or entrada == "." or entrada == ";":
				estado = "qr"
			    	print "caracter invalido::.  " + entrada
		elif estado == "q1":
			if entrada == ";":
				estado = "qr"
			    	print "caracter invalido::.  " + entrada
			if entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" or entrada=="0" or entrada ==",":
                		estado = "q1"
			    	n1 += entrada

		    	if entrada == "*" or entrada == "+" or entrada == "-" or entrada == "/":
			    	estado = "q2"
			    	o += entrada
            		if entrada == ";":
                		estado = "qr"
				print "caracter invalido::.  " +  entrada

	    	elif estado == "q2":
			if entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" or entrada=="0":
				estado = "q3"
			    	n2 += entrada

		   	if entrada == "*" or entrada == "+" or entrada == "-" or entrada == "/":
			    	estado = "qr"
			    	print "caracter invalido::.  " + entrada

	    	elif estado == "q3":
            		if entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" or entrada=="0" or entrada == "*" or entrada == "+" or entrada == "-" or entrada == "/":
                		estado = "q3"
				n2 += entrada
		    	if entrada=="*" or entrada == "/" or entrada == "+" or entrada == "-":
			    	estado ="qr"
		    	if entrada == ";":
			    	estado = "qa"
			    	n1 = int(n1)
			    	n2= int(n2)
			    	if o == "*":
					res = n1 * n2
			    	if o=="/":
				    	res=n1/n2
			    	if o=="+":
				    	res=n1+n2
			    	if o == "-":
				    	res=n1-n2
			    	print "el resultado es ::.  " + str(res)

	
	print estado
	i += 1
