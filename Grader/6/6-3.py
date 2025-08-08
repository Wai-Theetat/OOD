def encode_msg(msg, roter, ind = 0):	#(roter + ind)%26
 
	l = "abcdefghijklmnopqrstuvwxyz"
	u = "ABCDEFGHIJKLMNOPQRSTUVXXYZ"
	n = len(msg)

	if ind < n:
		#make it modifiable
		msg = list(msg)

		if msg[ind] in l:			
			alph_pos = ord(msg[ind]) - ord('a')
			rotation_value = (roter + ind)%26
			new_alph_pos = (alph_pos + rotation_value)%26
			
   
			if alph_pos == new_alph_pos:
				roter += 1
				new_alph_pos = (new_alph_pos + 1)%26
    
			msg[ind] = chr(new_alph_pos + ord('a'))
	
 	
		elif msg[ind] in u:
			alph_pos = ord(msg[ind]) - ord('A')
			rotation_value = (roter + ind)%26
			new_alph_pos = (alph_pos + rotation_value)%26
			
   
			if alph_pos == new_alph_pos:
				roter += 1
				new_alph_pos = (new_alph_pos + 1)%26
    
			msg[ind] = chr(new_alph_pos + ord('A'))
	
		else:
			return encode_msg(msg, roter, ind + 1)

		return encode_msg(msg, roter, ind + 1)

	else:
		msg = "".join(msg)
		return msg

def decode_msg(msg, roter, ind = 0): 
	
	l = "abcdefghijklmnopqrstuvwxyz"
	u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	n = len(msg)

	if ind < n:
		#make it modifiable
		msg = list(msg)

		if msg[ind] in l:			
			alph_pos = ord(msg[ind]) - ord('a')
			rotation_value = (roter + ind)%26
			new_alph_pos = (alph_pos - rotation_value)%26
			
			#print(alph_pos, roter, rotation_value , new_alph_pos, chr(new_alph_pos + 97))
  
			if alph_pos == new_alph_pos:
				roter += 1
				new_alph_pos = (new_alph_pos - 1)%26
    
			msg[ind] = chr(new_alph_pos + ord('a'))
  
		elif msg[ind] in u:
			alph_pos = ord(msg[ind]) - ord('A')
			rotation_value = (roter + ind)%26
			new_alph_pos = (alph_pos - rotation_value)%26
			
			#print(alph_pos, roter, rotation_value , new_alph_pos, chr(new_alph_pos + 97))
  
			if alph_pos == new_alph_pos:
				roter += 1
				new_alph_pos = (new_alph_pos - 1)%26
    
			msg[ind] = chr(new_alph_pos + ord('A'))
		
		return decode_msg(msg, roter, ind + 1)

	else:
		msg = "".join(msg)
		return msg

def main():
	print("This is Caesar cipher")
    
	msg, roter = input("Enter Input : ").split(',')
    
	encoded = encode_msg(msg, int(roter))
	print(f"Encoded Message: {encoded}")
    
	decoded = decode_msg(encoded, int(roter))	
	print(f"Decoded Message: {decoded}")
    
main()