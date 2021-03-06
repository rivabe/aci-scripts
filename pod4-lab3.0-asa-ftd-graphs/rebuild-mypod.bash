#!/bin/bash
################################################################################
#                                                                              #
# Copyright (c) 2017 Cisco Systems                                             #
# All Rights Reserved.                                                         #
#                                                                              #
#    Licensed under the Apache License, Version 2.0 (the "License"); you may   #
#    not use this file except in compliance with the License. You may obtain   #
#    a copy of the License at                                                  #
#                                                                              #
#         http://www.apache.org/licenses/LICENSE-2.0                           #
#                                                                              #
#    Unless required by applicable law or agreed to in writing, software       #
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT #
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the  #
#    License for the specific language governing permissions and limitations   #
#    under the License.                                                        #
#                                                                              #
################################################################################

path=""
for i in (4..4);
do
   echo -e " \nWelcome to your ACI pod, please follow these steps to orchestrate security in your tenant pod$i.\n";
   echo -e " - If any of these steps fail with python errors, please contact your proctor with a step that failed.";
   echo -e " - Note that each step script will dump the xml code being applied to your APIC and tenant pod$i.";
   echo -e " - To bring your tenant pod$i to a starting config it has now, you can reboot api-client vm using your vCenter.";
   echo -e " - Press Enter to continue and execute each step script.";
   echo -e " \n1. Create tenant, app profiles, epgs, bd, vrf: [continue]"; read go
   python ${path}faba-tenant-apps.py $i $i

   echo -e " \n2. Create device mgr and ftdv device as L4-L7 device: [continue]"; read go
   python ${path}faba-ftdv-devmgr.py $i $i
   python ${path}faba-ftdv-dev.py $i $i

   echo -e " \n3. Create ftdv - function profile: [continue]"; read go
   python ${path}faba-ftd-l3-fprof.py $i $i
   
   echo -e " \n4. Add service graph: [continue]"; read go
   python ${path}faba-ftdv-graph.py $i $i

   echo -e " \n5. Apply ftdv SG and create app-to-db contract: [continue]"; read go
   python ${path}faba-ftdv-apply-graph.py $i $i

   echo -e "\n 6. Create PBR BD for ASA failover context device: [continue]"; read go
   python faba-asa-fover-pbr-bd.py $i $i

   echo -e "\n 7. Create PBR redirect IP/MAC info: [continue]"; read go
   python ${path}faba-pbr-redirect.py $i $i

   echo -e "\n 8. Create/Register ASA device (context): [continue]"; read go
   python ${path}faba-asa-pbr-device.py $i $i

   echo -e "\n 9. Create ASA device config (function profile): [continue]"; read go
   python ${path}faba-pbr-fprof.py $i $i

   echo -e "\n 10. Create ASA device PBR service graph: [continue]"; read go
   python ${path}faba-asa-pbr-graph.py $i $i

   echo -e "\n 11. Apply service graph via wizard that also creates contract, filter, and attache the graph: [continue]"; read go
   python ${path}faba-asa-pbr-apply-graph.py $i $i

   echo -e "\n 12. Add ARP no redirect subject to the contract: [continue]"; read go
   python ${path}faba-arp-subject.py $i $i

   echo -e "\n 13. Update selection policy w/ one-arm information: [continue]"; read go
   python ${path}faba-asa-pbr-sel-policy.py $i $i

   echo -e "\n14. Create ASA cluster context as L4-L7 device: [continue]"; read go
   python ${path}faba-asa-cluster-pods.py $i $i
   
   echo -e "\n15. Create ASA cluster context config - function profile: [continue]"; read go
   python ${path}faba-asa-cluster-fprof.py $i $i

   echo -e "\n16. Create L3outs for fabric and ASA cluster context: [continue]"; read go
   python ${path}faba-l3out.py $i $i

   echo -e "\n17. Add service graph: [continue]"; read go
   python ${path}faba-asa-cluster-graph.py $i $i

   echo -e "\n18. Apply asa-cluster SG and create out-to-web contract: [continue]"; read go
   python ${path}faba-asa-cluster-apply-graph.py $i $i

   echo -e " \n19. We are done!  Now test your pod$i tenant EPG connectivity using these scripts on respective linux hosts:\n";
   echo -e "outside lnx: out-to-web_ping (also wget, ssh, udp)\n";
   echo -e "web lnx: out-to-web_ping web-to-app_ping (also wget, ssh, udp)\n";
   echo -e "app lnx: web-to-app_ping app-to-db_ping (also wget, ssh, udp)\n";
   echo -e "db lnx: app-to-db_ping (also wget, ssh, udp)\n";
   echo -e "Feel free to look into all scripts for your reference[continue]"; read go
   done
 
