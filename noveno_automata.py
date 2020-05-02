
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
					n1+=entrada
			if entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or  entrada=="j" or  entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z" or entrada==".":

					estado = "q2"
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

		    if entrada == " ":
			    	estado = "q3"


			if entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or  entrada=="j" or  entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z" or entrada==".":

					estado = "qr"
					print "caracter invalido" + entrada


	    	elif estado == "q2":

			if entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or  entrada=="j" or  entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z":

				estado = "q2"
				n1 += entrada

		   	if entrada == " ":
			    	estado = "q3"
			if entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" or entrada=="0":
			    	estado = "qr"
			if entrada == ";":
				estado = "qr"

	    	elif estado == "q3":
            		if entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" or entrada=="0" or entrada == "*" or entrada == "+" or entrada == "-" or entrada == "/":
                		estado = "qr"
				print "caracter invalido" + entrada
		    	if entrada=="*" or entrada == "/" or entrada == "+" or entrada == "-":
			    	estado ="q4"
				o += entrada
			if entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or  entrada=="j" or  entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z":
			    	estado = "q5"
				o += entrada
		    	if entrada == ";":
			    	estado = "qr"
				print "caracter invalido" + entrada
			if entrada ==" ":
			        estado = "qr"
				print "caracter invalido" + entrada
		elif estado=="q4":
		        if entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or  entrada=="j" or  entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z":
		                estado = "qr"
				print "caracter invalido" + entrada
		        if entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" or entrada=="0" or entrada == "*" or entrada == "+" or entrada == "-" or entrada == "/":
		            	estado ="qr"
				print "caracter invalido" + entrada
		        if entrada == " ":
		            	estado ="q6"

		elif estado=="q5":
			if entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or  entrada=="j" or  entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z":
		                estado = "q5"
				o += entrada
		        if entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" or entrada=="0" or entrada == "*" or entrada == "+" or entrada == "-" or entrada == "/":
		            	estado ="qr"
				print "caracter invalido" + entrada
		        if entrada == " ":
		            	estado ="q6"
			if entrada =="+" or entrada == "-" or entrada == "/" or entrada == "*":
				estado = "qr" + entrada

		elif estado=="q6":
			if entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or  entrada=="j" or  entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z":
		        	estado = "q8"
				n2 += entrada
		        if entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" or entrada=="0":
		            	estado ="q7"
				n2 += entrada
		       	if entrada == " ":
		            	estado ="qr"
				print "caracter invalido" + entrada
		       	if  entrada == "*" or entrada == "+" or entrada == "-" or entrada == "/":
		            	estado ="qr"
				print "caracter invalido" + entrada
	            	if entrada ==";":
	                	estado = "qr"
				print "caracter invalido" + entrada

		elif estado=="q7":
		        if entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or  entrada=="j" or  entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z":
		        	estado = "qr"
				print "caracter invalido" + entrada
		        if entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" or entrada=="0":
		            	estado ="q7"
				n2 += entrada
		      	if entrada == " ":
		            	estado ="qr"
				print "caracter invalido" + entrada
		       	if entrada == "*" or entrada == "+" or entrada == "-" or entrada == "/":
		            	estado ="qr"
				print "caracter invalido" + entrada
	            	if entrada ==";":
	                	estado = "qa"


		elif estado=="q8":
			if entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or  entrada=="j" or  entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z":
		                estado = "q8"
				n2 += entrada
		        if entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" or entrada=="0":
		            	estado ="qr"
				print "caracter invalido" + entrada
		       	if entrada == " ":
		            	estado ="qr"
				print "caracter invalido" + entrada
		       	if entrada == "*" or entrada == "+" or entrada == "-" or entrada == "/":
		            	estado ="qr"
				print "caracter invalido" + entrada
	            	if entrada ==";":
	                	estado = "qa"

	print estado
	i += 1
