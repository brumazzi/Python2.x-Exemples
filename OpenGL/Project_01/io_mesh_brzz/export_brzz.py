import bpy

objName = []
vertex = []
faces = []
vl = []
nl = []
uvl = []
objMtx = []
objCnt = 0
maxVcnt = 0

def r3d(v):
	return round(v[0],6),round(v[1],6),round(v[2],6)

def r2d(v):
	return round(v[0],6), round(v[1],6)


def clearName(name):
	tmp = name.upper()
	ret = ""
	for i in tmp:
		if(i in " ./\-+#$%^!@&()"):
			ret = ret + "_"
		else:
			ret = ret + i
	return ret

def buildData(obj,msh,name):
	global objCnt
	global objName
	global vertex
	global faces
	global vl
	global nl
	global uvl
	global objMtx

	lvdic = {}
	lfl = []
	lvl = []
	lnl = []
	luvl = []
	lvcnt = 0
	isSmooth = False
	hasUV = True

	print("Building for: %s\n" %obj.name)

	if (len(msh.tessface_uv_textures)>0):
		if(msh.tessface_uv_textures.active is None):
			hasUV = False
	else:
		hasUV = False

	if hasUV:
		activeUV = msh.tessface_uv_textures.active.data

	objName.append(clearName(name))
	objCnt+=1

	for i,f in enumerate(msh.tessfaces):
		isSmooth = f.use_smooth
		tmpFaces = []
		for h,v in enumerate(f.vertices):
			vec = msh.vertices[v].co
			vec = r3d(vec)

			if(isSmooth):
				nor = msh.vertices[v].normal
			else:
				nor = f.normal
			nor = r3d(nor)

			if(hasUV):
				print(activeUV[i].uv[h])
				co = activeUV[i].uv[h]
				co = r2d(co)
			else:
				co = (0.0,0.0)

			key = vec,nor,co
			vinx = lvdic.get(key)

			if (vinx is None):
				lvdic[key] = lvcnt
				lvl.append(vec)
				lnl.append(nor)
				luvl.append(co)
				tmpFaces.append(lvcnt)
				lvcnt+=1
			else:
				inx = lvdic[key]
				tmpFaces.append(inx)

		if (len(tmpFaces) == 3):
			lfl.append(tmpFaces)
		else:
			lfl.append([tmpFaces[0],tmpFaces[1],tmpFaces[2]])
			lfl.append([tmpFaces[0],tmpFaces[2],tmpFaces[3]])

	vertex.append(lvdic)
	faces.append(lfl)
	vl.append(lvl)
	nl.append(lnl)
	uvl.append(luvl)
	objMtx.append(obj.matrix_local)

##################################################
##		ESCREVE NO ARQUIVO		##
##################################################

def writeFile(file):
	file.write('!OGLModel BRZZ\n')
	file.write('Model_Name: %s\n' % objName[0].lower())
	file.write('Total_Vertex: %i\n' % len(vl[0]))
	file.write('Total_Faces: %i\n' % len(faces[0]))
#	print("vl =",len(vl[0]))
#	print("objName =",objName[0].lower())
#	print("faces =",len(faces[0]))
	for i,d in enumerate(vl):
		for j in range(0,len(d)):
			file.write('& %f %f %f '%tuple(vl[i][j]))
			file.write('%f %f %f '%tuple(nl[i][j]))
			file.write('%f %f\n'%tuple(uvl[i][j]))

	#file.write('$')

def save(filename):
	file = open(filename,'w',newline="\n")
	writeFile(file)
	file.close()

def export(filename="untitled.brzz",entire_scene=True):
	global objCnt
	global objName
	global vertex
	global faces
	global vl
	global nl
	global uvl
	global objMtx

	print("------------------------------------------------------\n")
	print("Starting script:\n")
	print(filename)

	objName = []
	vertex = []
	faces = []
	vl = []
	nl = []
	uvl = []
	objMtx = []
	objCnt = 0
	maxVcnt = 0

	sc = bpy.context.scene

	if (entire_scene):
		for o in sc.objects:
			if (o.type == "MESH"):
				msh = o.to_mesh(sc,True,"PREVIEW")
				buildData(o,msh,o.name)
				bpy.data.meshes.remove(msh)
	else:
		o = sc.objects.active
		msh = o.to_mesh(sc,True,'PREVIEW')
		buildData(o,msh,o.name)
		bpy.data.meshes.remove(msh)

	save(filename)
	print("Done\n")
	return {'FINISHED'}

