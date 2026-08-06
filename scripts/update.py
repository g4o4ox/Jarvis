import subprocess 


print("Updating System")

subprocess.run("sudo pacman -S Syu")

print("updated")
