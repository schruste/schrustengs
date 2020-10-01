import meshio
import os

def VTKOutputToVTU():
  def convert_vtk_to_vtu(basename):
      m = meshio.read(basename+".vtk")
      meshio.write(basename+".vtu",m)
      # os.system("meshio-convert "+basename+".vtk "+basename+".vtu")
      # os.system("meshio-compress "+basename+".vtu > /dev/null")
      os.remove(basename+".vtk")
  
  
  from ngsolve import VTKOutput
  
  oldDo = VTKOutput.Do
  
  def newDo(*args, **kwargs):
      name = oldDo(*args, **kwargs)
      convert_vtk_to_vtu(name)
  print("patching VTKOutput to convert output from vtk to vtu")
  VTKOutput.Do = newDo    
  
VTKOutputToVTU()
