namespace_kinds = {
	chr(0x08): 'CONSTANT_Namespace',
	chr(0x16): 'CONSTANT_PackageNamespace',
	chr(0x17): 'CONSTANT_PackageInternalNs',
	chr(0x18): 'CONSTANT_ProtectedNamespace',
	chr(0x19): 'CONSTANT_ExplicitNamespace',
	chr(0x1A): 'CONSTANT_StaticProtectedNs',
	chr(0x05): 'CONSTANT_PrivateNs' }
		
def getNamespace(data):
	kind = data.f.read(1)
	if 8 in namespace_kinds:
		kind = namespace_kinds[kind]
	else:
		kind = kind

	name_index = data.readEncodedU32()
	return [ kind, name_index ]
