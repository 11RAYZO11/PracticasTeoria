def p_operacion(p):
	"""operacion : n1 op n2"""
	p[0] = [p[1], p[2], p[3]]
	print p[0]
def p_n1(p):
	"""n1 : palabra
		| numero"""
	p[0] = p[1]
def p_op(p):
	"""op : simbolo
		| palabra"""
	p[0] = p[1]
def p_n2(p):
	"""n2 : palabra
		| numero"""
	p[0] = p[1]
def p_palabra(p):
	"""palabra : pal"""
	p[0] = p[1]
def p_simbolo(p):
	"""simbolo : suma
		| resta
		| mul
		| div"""
	p[0] = p[1]
def p_numero(p):
	"""numero : num"""
	p[0] = p[1]
def p_error(p):
	print"error de sintaxis"
	print p
