#!/usr/bin/env python
'''
Autogenerated code using arya
Original Object Document Input: 
'''
# list of packages that should be imported for this code to work
import cobra.mit.access
import cobra.mit.request
import cobra.mit.session
import cobra.model.fv
import cobra.model.pol
import cobra.model.vns
import sys
from cobra.internal.codec.xmlcodec import toXMLStr

pod_num_start = int(sys.argv[1])
pod_num_end = int(sys.argv[2])
ctx_ip_standby = 80
ctx_ip_active = 80
admin_ip = 22

# log into an APIC and create a directory object
ls = cobra.mit.session.LoginSession('https://10.10.35.10', 'pod%s' % pod_num_end, 'cisco')
md = cobra.mit.access.MoDirectory(ls)
md.login()

for pod_num in range(pod_num_start, (1 + pod_num_end)):
    # the top level object on which operations will be made
    polUni = cobra.model.pol.Uni('')
    fvTenant = cobra.model.fv.Tenant(polUni, 'pod%d' % pod_num)
    if pod_num >= 21:
        admin_ip = 26
    # build the request using cobra syntax
    vnsLDevVip = cobra.model.vns.LDevVip(fvTenant, name=u'pod%d-asa-fover' % pod_num, funcType=u'GoTo', devtype=u'PHYSICAL', contextAware=u'single-Context', mode=u'legacy-Mode')
    vnsRsMDevAtt = cobra.model.vns.RsMDevAtt(vnsLDevVip, tDn=u'uni/infra/mDev-CISCO-ASA-1.2')
    vnsCCred = cobra.model.vns.CCred(vnsLDevVip, name=u'username', value=u'aciadmin')
    vnsCCredSecret = cobra.model.vns.CCredSecret(vnsLDevVip, name=u'password', value=u'cisco')
    vnsCMgmt = cobra.model.vns.CMgmt(vnsLDevVip, host=u'10.10.10.%d' % admin_ip, name=u'', port=u'443') 
    vnsRsALDevToPhysDomP = cobra.model.vns.RsALDevToPhysDomP(vnsLDevVip, tDn=u'uni/phys-asa_fover')
    vnsChkr = cobra.model.vns.Chkr(vnsLDevVip, name=u'')
    vnsCDev = cobra.model.vns.CDev(vnsLDevVip, vcenterName=u'', vmName=u'', name=u'pod%d-asa-fover_Device_2' % pod_num, devCtxLbl=u'') 
    vnsCCred2 = cobra.model.vns.CCred(vnsCDev, name=u'username', value=u'aciadmin')
    vnsCCredSecret2 = cobra.model.vns.CCredSecret(vnsCDev, name=u'password', value=u'cisco')
    vnsCMgmt2 = cobra.model.vns.CMgmt(vnsCDev, host=u'10.10.11.%d' % (ctx_ip_standby + pod_num), name=u'', port=u'443') 
    vnsCIf = cobra.model.vns.CIf(vnsCDev, name=u'GigabitEthernet0/1', vnicName=u'')
    vnsRsCIfPathAtt = cobra.model.vns.RsCIfPathAtt(vnsCIf, tDn=u'topology/pod-1/paths-101/pathep-[eth1/30]')
    vnsCIf2 = cobra.model.vns.CIf(vnsCDev, name=u'GigabitEthernet0/0', vnicName=u'')
    vnsRsCIfPathAtt2 = cobra.model.vns.RsCIfPathAtt(vnsCIf2, tDn=u'topology/pod-1/paths-101/pathep-[eth1/29]')
    vnsCDev2 = cobra.model.vns.CDev(vnsLDevVip, vcenterName=u'', vmName=u'', name=u'pod%d-asa-fover_Device_1'  % pod_num, devCtxLbl=u'')
    vnsCCred3 = cobra.model.vns.CCred(vnsCDev2, name=u'username', value=u'aciadmin')
    vnsCCredSecret3 = cobra.model.vns.CCredSecret(vnsCDev2, name=u'password', value=u'cisco')
    vnsCMgmt3 = cobra.model.vns.CMgmt(vnsCDev2, host=u'10.10.10.%d' % (ctx_ip_active + pod_num), name=u'', port=u'443') 
    vnsCIf3 = cobra.model.vns.CIf(vnsCDev2, name=u'GigabitEthernet0/1', vnicName=u'')
    vnsRsCIfPathAtt3 = cobra.model.vns.RsCIfPathAtt(vnsCIf3, tDn=u'topology/pod-1/paths-101/pathep-[eth1/26]')
    vnsCIf4 = cobra.model.vns.CIf(vnsCDev2, name=u'GigabitEthernet0/0', vnicName=u'')
    vnsRsCIfPathAtt4 = cobra.model.vns.RsCIfPathAtt(vnsCIf4, tDn=u'topology/pod-1/paths-101/pathep-[eth1/25]')
    vnsLIf = cobra.model.vns.LIf(vnsLDevVip, name=u'external')
    vnsRsMetaIf = cobra.model.vns.RsMetaIf(vnsLIf, tDn=u'uni/infra/mDev-CISCO-ASA-1.2/mIfLbl-external')
    vnsRsCIfAtt = cobra.model.vns.RsCIfAtt(vnsLIf, tDn=u'uni/tn-pod%d/lDevVip-pod%d-asa-fover/cDev-pod%d-asa-fover_Device_1/cIf-[GigabitEthernet0/1]' % (pod_num, pod_num, pod_num)) 
    vnsRsCIfAtt2 = cobra.model.vns.RsCIfAtt(vnsLIf, tDn=u'uni/tn-pod%d/lDevVip-pod%d-asa-fover/cDev-pod%d-asa-fover_Device_2/cIf-[GigabitEthernet0/1]' % (pod_num, pod_num, pod_num))
    vnsLIf2 = cobra.model.vns.LIf(vnsLDevVip, name=u'internal')
    vnsRsMetaIf2 = cobra.model.vns.RsMetaIf(vnsLIf2, tDn=u'uni/infra/mDev-CISCO-ASA-1.2/mIfLbl-internal')
    vnsRsCIfAtt3 = cobra.model.vns.RsCIfAtt(vnsLIf2, tDn=u'uni/tn-pod%d/lDevVip-pod%d-asa-fover/cDev-pod%d-asa-fover_Device_2/cIf-[GigabitEthernet0/0]' % (pod_num, pod_num, pod_num))
    vnsRsCIfAtt4 = cobra.model.vns.RsCIfAtt(vnsLIf2, tDn=u'uni/tn-pod%d/lDevVip-pod%d-asa-fover/cDev-pod%d-asa-fover_Device_1/cIf-[GigabitEthernet0/0]' % (pod_num, pod_num, pod_num))


    # commit the generated code to APIC
    print toXMLStr(fvTenant)
    c = cobra.mit.request.ConfigRequest()
    c.addMo(fvTenant)
    md.commit(c)
