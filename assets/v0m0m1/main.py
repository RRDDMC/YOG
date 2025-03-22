from panda3d.core import GeomVertexData, GeomVertexFormat, Geom, GeomTriangles, GeomVertexWriter, GeomNode, Texture, TextureAttrib, NodePath, RenderState, ModelRoot
from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):

	def __init__(self):
		ShowBase.__init__(self)

		# Creating vertex data.
		vdata = GeomVertexData('name', GeomVertexFormat.getV3n3t2(), Geom.UHStatic)
		vdata.setNumRows(3)

		vertex = GeomVertexWriter(vdata, 'vertex')
		normal = GeomVertexWriter(vdata, 'normal')
		texcoord = GeomVertexWriter(vdata, 'texcoord')

		# Adding vertex data.
		
		#Bottom
		vertex.addData3(-1, -1, -1)
		normal.addData3(0, 0, -1)
		texcoord.addData2(0.5, 0.75)
		
		vertex.addData3(1, -1, -1)
		normal.addData3(0, 0, -1)
		texcoord.addData2(0.75, 0.75)
		
		vertex.addData3(1, 1, -1)
		normal.addData3(0, 0, -1)
		texcoord.addData2(0.75, 1)
		
		vertex.addData3(-1, 1, -1)
		normal.addData3(0, 0, -1)
		texcoord.addData2(0.5, 1)
		
		#Top
		vertex.addData3(-1, -1, 1)
		normal.addData3(0, 0, 1)
		texcoord.addData2(0, 0.25)
		
		vertex.addData3(1, -1, 1)
		normal.addData3(0, 0, 1)
		texcoord.addData2(0.25, 0.25)
		
		vertex.addData3(1, 1, 1)
		normal.addData3(0, 0, 1)
		texcoord.addData2(0.25, 0.5)
		
		vertex.addData3(-1, 1, 1)
		normal.addData3(0, 0, 1)
		texcoord.addData2(0, 0.5)
		
		#Blue side
		vertex.addData3(-1, -1, -1)
		normal.addData3(0, 1, 0)
		texcoord.addData2(0, 0.75)

		vertex.addData3(1, -1, -1)
		normal.addData3(0, 1, 0)
		texcoord.addData2(0.25, 0.75)

		vertex.addData3(1, -1, 1)
		normal.addData3(0, 1, 0)
		texcoord.addData2(0.25, 1)

		vertex.addData3(-1, -1, 1)
		normal.addData3(0, 1, 0)
		texcoord.addData2(0, 1)
		
		#Green side
		vertex.addData3(-1, 1, -1)
		normal.addData3(0, 1, 0)
		texcoord.addData2(0, 0.5)
		
		vertex.addData3(-1, -1, -1)
		normal.addData3(0, 1, 0)
		texcoord.addData2(0.25, 0.5)
		
		vertex.addData3(-1, -1, 1)
		normal.addData3(0, 1, 0)
		texcoord.addData2(0.25, 0.75)
		
		vertex.addData3(-1, 1, 1)
		normal.addData3(0, 1, 0)
		texcoord.addData2(0, 0.75)

		#Yellow side
		vertex.addData3(1, 1, -1)
		normal.addData3(0, 1, 0)
		texcoord.addData2(0.25, 0.75)
		
		vertex.addData3(-1, 1, -1)
		normal.addData3(0, 1, 0)
		texcoord.addData2(0.5, 0.75)
		
		vertex.addData3(-1, 1, 1)
		normal.addData3(0, 1, 0)
		texcoord.addData2(0.5, 1)
		
		vertex.addData3(1, 1, 1)
		normal.addData3(0, 1, 0)
		texcoord.addData2(0.25, 1)
		
		#Red side
		vertex.addData3(1, -1, -1)
		normal.addData3(0, 1, 0)
		texcoord.addData2(0.25, 0.5)
		
		vertex.addData3(1, 1, -1)
		normal.addData3(0, 1, 0)
		texcoord.addData2(0.5, 0.5)
		
		vertex.addData3(1, 1, 1)
		normal.addData3(0, 1, 0)
		texcoord.addData2(0.5, 0.75)
		
		vertex.addData3(1, -1, 1)
		normal.addData3(0, 1, 0)
		texcoord.addData2(0.25, 0.75)
		
		# Creating primitive - a.
		prim_a = GeomTriangles(Geom.UHStatic)
		prim_a.addVertices(2, 1, 0)
		prim_a.addVertices(3, 2, 0)
		prim_a.addVertices(4, 5, 6)
		prim_a.addVertices(4, 6, 7)
		prim_a.addVertices(8, 9, 10)
		prim_a.addVertices(8, 10, 11)
		prim_a.addVertices(12, 13, 14)
		prim_a.addVertices(12, 14, 15)
		prim_a.addVertices(16, 17, 18)
		prim_a.addVertices(16, 18, 19)
		prim_a.addVertices(20, 21, 22)
		prim_a.addVertices(20, 22, 23)
		prim_a.closePrimitive()

		geom1 = Geom(vdata)
		geom1.addPrimitive(prim_a)


		# Load texture.
		tex1 = Texture("Texture")
		#tex1.read('BaseTextureModel.png')
		tex1.read('grassSummer.png')
		tex1.setMagfilter(Texture.FTNearest)
		tex1.setMinfilter(Texture.FTNearest)

		# Create new geom state.
		state_a = RenderState.make(TextureAttrib.make(tex1))

		# Create geom node.
		geom_node = GeomNode('Plane')
		geom_node.add_geom(geom1, state_a)

		# Attach geom node.
		root = NodePath(geom_node)
		root.reparent_to(render)
		root.writeBamFile("test.bam")

app = MyApp()
app.run()
