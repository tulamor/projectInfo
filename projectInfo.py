

def process_USED_BY(data, pack):
  packs = []
  str = "%s_USED_BY = " % pack
  if "USED_BY" in data["DEPS"][pack]:
    for  d in data["DEPS"][pack]["USED_BY"]:
      push data["DEPS"][d] packs
    str =join(" ", packs.sorted())
  print str

def process_ORIGIN(data, prod):
  str = "%s_ORIGIN = " % prod
  if "ORIGIN" in data["PROD"][prod]
    for dir in data["PROD"][prod]["ORIGIN"]
      tool = data["PROD"][prod]["ORIGIN"][dir]
    str .= os.path.join(tool, dir)
  print str

def process_USES(data, pack):
  packs = []
  str = "%s_USES = " % pack
  if data["DATA"][pack]["USES"]
    for d in data["DATA"][pack]["USES"]
      push os.path.join(data["DEPS"][d]["TYPE"], d) packs
    str = join(" ", packs.sorted())
  print(str)

def FixToolName(t):
  lct = lc(t)
  if lct in tools["SETUP"]: return lct
  return t

def updateSCRAMTool(tool, base, data):
  file = os.path.join(base, ".SCRAM", arch, "ProjectCache.%s" % cacheetext)
  c = data2json(file)
  data["FILES"][file] = "1"
  for dir in c["BUILDTREE"]
    if dc["RAWDATA"] & dc["RAWDATA"]["DEPENDENCIES"]
      class = dc["CLASS"]
      prod = None
      if re.search(r'^(LIBRARY|CLASSLIB|SEAL_PLATFORM)$'):
        dir = dc["PARENT"]
        prod = dc["NAME"]
        data["DATA"][dir]["USES"] = {}
        data["DATA"][dir]["TYPE"] = tool
        dc = dc["RAWDATA"]["DEPENDENCIES"]
        for d in dc:
          data["DATA"][dir]["USES"][FixToolName(d)] = "1"
          if prod: data["PROD"][prod]["ORIGIN"][dir] = tool
          else:
            dc = c["BUILDTREE"][dir]["RAWDATA"]
            if dc["content"]["BUILDPRODUCTS"]
              dc = dc["content"]["BUILDPRODUCTS"]
              for type in ("LIBRARY", "BIN"):
                if type in dc:
                  for prod in dc[type]
                    data["PROD"][prod]["ORIGIN"][dir] = tool



def updateDeps(data, pack):
  if not pack:
    for d in data["DATA"]: updateDeps(data, d)
    return 0
  if pack in data["DEPS"]: return 0
  data["DEPS"]