import subprocess

# Define VM parameters
vm_name = "MyVM2"
os_type = "Linux"
memory_size = 1024  # in MB
cpu_count = 2

# Construct the VBoxManage command to create the VM
create_vm_command = f"VBoxManage createvm --name {vm_name} --ostype {os_type} --register"
subprocess.run(create_vm_command, shell=True, check=True)

# Set VM memory and CPU
modify_vm_command = f"VBoxManage modifyvm {vm_name} --memory {memory_size} --cpus {cpu_count}"
subprocess.run(modify_vm_command, shell=True, check=True)

# Enable IO APIC
enable_ioapic_command = f"VBoxManage modifyvm {vm_name} --ioapic on"
subprocess.run(enable_ioapic_command, shell=True, check=True)

# Add VMSVGA display adapter
add_vmsvga_display_command = f"VBoxManage modifyvm {vm_name} --graphicscontroller vmsvga"
subprocess.run(add_vmsvga_display_command, shell=True, check=True)

print(f"VM '{vm_name}' created successfully with IO APIC and VMSVGA display adapter enabled.")
