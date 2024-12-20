################################################################################
# Purpose:
#   Rename Bones (The King of Fighters: All-Stars) to a Blender friendly names
#
# Usage:
#	Select an armature imported form asset from The King of Fighters: All-Stars
#	Select the armature and run this script, all bones renamed to their a Blender Friendly counterparts
################################################################################

names = dict()

#names['CH054_000_U_S']                  = 'CH054_000_U_S'
#names['Translate']                      = 'Translate'
#names['Bip001']                         = 'Bip001'
#names['Rig_Root']                       = 'Rig_Root'
#names['Bip_General']                    = 'Bip_General'
#names['Bip_New']                        = 'Bip_New'


# Old like (Maya's Defaults)
names['Bip001 Pelvis']                  = 'Spine'
names['Bip001 Spine']                   = 'Spine1'
names['Bip001 Spine1']                  = 'Spine4'
names['Bip001 Neck']                    = 'Neck1'
names['Bip001 Head']                    = 'Head1'

names['Bip001 L Finger0']               = 'Finger0_L'
names['Bip001 L Finger01']              = 'Finger01_L'
names['Bip001 L Finger02']              = 'Finger02_L'
names['Bip001 L Finger1']               = 'Finger1_L'
names['Bip001 L Finger11']              = 'Finger11_L'
names['Bip001 L Finger12']              = 'Finger12_L'
names['Bip001 L Finger2']               = 'Finger2_L'
names['Bip001 L Finger21']              = 'Finger21_L'
names['Bip001 L Finger22']              = 'Finger22_L'
names['Bip001 L Finger3']               = 'Finger3_L'
names['Bip001 L Finger31']              = 'Finger31_L'
names['Bip001 L Finger32']              = 'Finger32_L'
names['Bip001 L Finger4']               = 'Finger4_L'
names['Bip001 L Finger41']              = 'Finger41_L'
names['Bip001 L Finger42']              = 'Finger42_L'

names['Bip001 R Finger0']               = 'Finger0_R'
names['Bip001 R Finger01']              = 'Finger01_R'
names['Bip001 R Finger02']              = 'Finger02_R'
names['Bip001 R Finger1']               = 'Finger1_R'
names['Bip001 R Finger11']              = 'Finger11_R'
names['Bip001 R Finger12']              = 'Finger12_R'
names['Bip001 R Finger2']               = 'Finger2_R'
names['Bip001 R Finger21']              = 'Finger21_R'
names['Bip001 R Finger22']              = 'Finger22_R'
names['Bip001 R Finger3']               = 'Finger3_R'
names['Bip001 R Finger31']              = 'Finger31_R'
names['Bip001 R Finger32']              = 'Finger32_R'
names['Bip001 R Finger4']               = 'Finger4_R'
names['Bip001 R Finger41']              = 'Finger41_R'
names['Bip001 R Finger42']              = 'Finger42_R'

names['Bip001 L Clavicle']              = 'Clavicle_L'
names['Bip001 L UpperArm']              = 'UpperArm_L'
names['Bip001 L Forearm']               = 'Forearm_L'
names['Bip001 L Hand']                  = 'Hand_L'

names['Bip001 R Clavicle']              = 'Clavicle_R'
names['Bip001 R UpperArm']              = 'UpperArm_R'
names['Bip001 R Forearm']               = 'Forearm_R'
names['Bip001 R Hand']                  = 'Hand_R'

names['Bip001 L Thigh']                 = 'Thigh_L'
names['Bip001 L Calf']                  = 'Calf_L'
names['Bip001 L Foot']                  = 'Foot_L'
names['Bip001 L Toe0']                  = 'Toe0_L'

names['Bip001 R Thigh']                 = 'Thigh_R'
names['Bip001 R Calf']                  = 'Calf_R'
names['Bip001 R Foot']                  = 'Foot_R'
names['Bip001 R Toe0']                  = 'Toe0_R'

names['Bip01 Pelvis']                   = 'Pelvis'
names['Bip01 Spine']                    = 'Spine1'
names['Bip01 Spine1']                   = 'Spine4'
names['Bip01 Neck']                     = 'Neck1'
names['Bip01 Head']                     = 'Head1'

names['Bip01 L Finger0']                = 'Finger0_L'
names['Bip01 L Finger01']               = 'Finger01_L'
names['Bip01 L Finger02']               = 'Finger02_L'
names['Bip01 L Finger1']                = 'Finger1_L'
names['Bip01 L Finger11']               = 'Finger11_L'
names['Bip01 L Finger12']               = 'Finger12_L'
names['Bip01 L Finger2']                = 'Finger2_L'
names['Bip01 L Finger21']               = 'Finger21_L'
names['Bip01 L Finger22']               = 'Finger22_L'
names['Bip01 L Finger3']                = 'Finger3_L'
names['Bip01 L Finger31']               = 'Finger31_L'
names['Bip01 L Finger32']               = 'Finger32_L'
names['Bip01 L Finger4']                = 'Finger4_L'
names['Bip01 L Finger41']               = 'Finger41_L'
names['Bip01 L Finger42']               = 'Finger42_L'

names['Bip01 R Finger0']                = 'Finger0_R'
names['Bip01 R Finger01']               = 'Finger01_R'
names['Bip01 R Finger02']               = 'Finger02_R'
names['Bip01 R Finger1']                = 'Finger1_R'
names['Bip01 R Finger11']               = 'Finger11_R'
names['Bip01 R Finger12']               = 'Finger12_R'
names['Bip01 R Finger2']                = 'Finger2_R'
names['Bip01 R Finger21']               = 'Finger21_R'
names['Bip01 R Finger22']               = 'Finger22_R'
names['Bip01 R Finger3']                = 'Finger3_R'
names['Bip01 R Finger31']               = 'Finger31_R'
names['Bip01 R Finger32']               = 'Finger32_R'
names['Bip01 R Finger4']                = 'Finger4_R'
names['Bip01 R Finger41']               = 'Finger41_R'
names['Bip01 R Finger42']               = 'Finger42_R'

names['Bip01 L Clavicle']               = 'Clavicle_L'
names['Bip01 L UpperArm']               = 'UpperArm_L'
names['Bip01 L Forearm']                = 'Forearm_L'
names['Bip01 L Hand']                   = 'Hand_L'

names['Bip01 R Clavicle']               = 'Clavicle_R'
names['Bip01 R UpperArm']               = 'UpperArm_R'
names['Bip01 R Forearm']                = 'Forearm_R'
names['Bip01 R Hand']                   = 'Hand_R'

names['Bip01 L Thigh']                  = 'Thigh_L'
names['Bip01 L Calf']                   = 'Calf_L'
names['Bip01 L Foot']                   = 'Foot_L'
names['Bip01 L Toe0']                   = 'Toe0_L'

names['Bip01 R Thigh']                  = 'Thigh_R'
names['Bip01 R Calf']                   = 'Calf_R'
names['Bip01 R Foot']                   = 'Foot_R'
names['Bip01 R Toe0']                   = 'Toe0_R'

names['Bip Pelvis']                     = 'Spine'
names['Bip Spine']                      = 'Spine1'
names['Bip Spine1']                     = 'Spine4'
names['Bip Neck']                       = 'Neck1'
names['Bip Head']                       = 'Head1'

names['Bip L Finger0']                  = 'Finger0_L'
names['Bip L Finger01']                 = 'Finger01_L'
names['Bip L Finger02']                 = 'Finger02_L'
names['Bip L Finger1']                  = 'Finger1_L'
names['Bip L Finger11']                 = 'Finger11_L'
names['Bip L Finger12']                 = 'Finger12_L'
names['Bip L Finger2']                  = 'Finger2_L'
names['Bip L Finger21']                 = 'Finger21_L'
names['Bip L Finger22']                 = 'Finger22_L'
names['Bip L Finger3']                  = 'Finger3_L'
names['Bip L Finger31']                 = 'Finger31_L'
names['Bip L Finger32']                 = 'Finger32_L'
names['Bip L Finger4']                  = 'Finger4_L'
names['Bip L Finger41']                 = 'Finger41_L'
names['Bip L Finger42']                 = 'Finger42_L'

names['Bip R Finger0']                  = 'Finger0_R'
names['Bip R Finger01']                 = 'Finger01_R'
names['Bip R Finger02']                 = 'Finger02_R'
names['Bip R Finger1']                  = 'Finger1_R'
names['Bip R Finger11']                 = 'Finger11_R'
names['Bip R Finger12']                 = 'Finger12_R'
names['Bip R Finger2']                  = 'Finger2_R'
names['Bip R Finger21']                 = 'Finger21_R'
names['Bip R Finger22']                 = 'Finger22_R'
names['Bip R Finger3']                  = 'Finger3_R'
names['Bip R Finger31']                 = 'Finger31_R'
names['Bip R Finger32']                 = 'Finger32_R'
names['Bip R Finger4']                  = 'Finger4_R'
names['Bip R Finger41']                 = 'Finger41_R'
names['Bip R Finger42']                 = 'Finger42_R'

names['Bip L Clavicle']                 = 'Clavicle_L'
names['Bip L UpperArm']                 = 'UpperArm_L'
names['Bip L Forearm']                  = 'Forearm_L'
names['Bip L Hand']                     = 'Hand_L'

names['Bip R Clavicle']                 = 'Clavicle_R'
names['Bip R UpperArm']                 = 'UpperArm_R'
names['Bip R Forearm']                  = 'Forearm_R'
names['Bip R Hand']                     = 'Hand_R'

names['Bip L Thigh']                    = 'Thigh_L'
names['Bip L Calf']                     = 'Calf_L'
names['Bip L Foot']                     = 'Foot_L'
names['Bip L Toe0']                     = 'Toe0_L'

names['Bip R Thigh']                    = 'Thigh_R'
names['Bip R Calf']                     = 'Calf_R'
names['Bip R Foot']                     = 'Foot_R'
names['Bip R Toe0']                     = 'Toe0_R'

# Somewhat ripped with Mesh prefix
names['Bip_General Pelvis']             = 'Pelvis'
names['Bip_General Spine']              = 'Spine1'
names['Bip_General Spine1']             = 'Spine4'
names['Bip_General Neck']               = 'Neck1'
names['Bip_General Head']               = 'Head1'

names['Bip_General L Clavicle']         = 'Clavicle_L'
names['Bip_General L UpperArm']         = 'UpperArm_L'
names['Bip_General L Forearm']          = 'Forearm_L'
names['Bip_General L Hand']             = 'Hand_L'

names['Bip_General R Clavicle']         = 'Clavicle_R'
names['Bip_General R UpperArm']         = 'UpperArm_R'
names['Bip_General R Forearm']          = 'Forearm_R'
names['Bip_General R Hand']             = 'Hand_R'

names['Bip_General L Finger0']          = 'Finger0_L'
names['Bip_General L Finger01']         = 'Finger01_L'
names['Bip_General L Finger02']         = 'Finger02_L'
names['Bip_General L Finger1']          = 'Finger1_L'
names['Bip_General L Finger11']         = 'Finger11_L'
names['Bip_General L Finger12']         = 'Finger12_L'
names['Bip_General L Finger2']          = 'Finger2_L'
names['Bip_General L Finger21']         = 'Finger21_L'
names['Bip_General L Finger22']         = 'Finger22_L'
names['Bip_General L Finger3']          = 'Finger3_L'
names['Bip_General L Finger31']         = 'Finger31_L'
names['Bip_General L Finger32']         = 'Finger32_L'
names['Bip_General L Finger4']          = 'Finger4_L'
names['Bip_General L Finger41']         = 'Finger41_L'
names['Bip_General L Finger42']         = 'Finger42_L'

names['Bip_General R Finger0']          = 'Finger0_R'
names['Bip_General R Finger01']         = 'Finger01_R'
names['Bip_General R Finger02']         = 'Finger02_R'
names['Bip_General R Finger1']          = 'Finger1_R'
names['Bip_General R Finger11']         = 'Finger11_R'
names['Bip_General R Finger12']         = 'Finger12_R'
names['Bip_General R Finger2']          = 'Finger2_R'
names['Bip_General R Finger21']         = 'Finger21_R'
names['Bip_General R Finger22']         = 'Finger22_R'
names['Bip_General R Finger3']          = 'Finger3_R'
names['Bip_General R Finger31']         = 'Finger31_R'
names['Bip_General R Finger32']         = 'Finger32_R'
names['Bip_General R Finger4']          = 'Finger4_R'
names['Bip_General R Finger41']         = 'Finger41_R'
names['Bip_General R Finger42']         = 'Finger42_R'

names['Bip_General L Thigh']            = 'Thigh_L'
names['Bip_General L Calf']             = 'Calf_L'
names['Bip_General L Foot']             = 'Foot_L'
names['Bip_General L Toe0']             = 'Toe0_L'

names['Bip_General R Thigh']            = 'Thigh_R'
names['Bip_General R Calf']             = 'Calf_R'
names['Bip_General R Foot']             = 'Foot_R'
names['Bip_General R Toe0']             = 'Toe0_R'

names['Bip_New Pelvis']                 = 'Pelvis'
names['Bip_New Spine']                  = 'Spine1'
names['Bip_New Spine1']                 = 'Spine4'
names['Bip_New Neck']                   = 'Neck1'
names['Bip_New Head']                   = 'Head1'

names['Bip_New L Clavicle']             = 'Clavicle_L'
names['Bip_New L UpperArm']             = 'UpperArm_L'
names['Bip_New L Forearm']              = 'Forearm_L'
names['Bip_New L Hand']                 = 'Hand_L'

names['Bip_New R Clavicle']             = 'Clavicle_R'
names['Bip_New R UpperArm']             = 'UpperArm_R'
names['Bip_New R Forearm']              = 'Forearm_R'
names['Bip_New R Hand']                 = 'Hand_R'

names['Bip_New L Finger0']              = 'Finger0_L'
names['Bip_New L Finger01']             = 'Finger01_L'
names['Bip_New L Finger02']             = 'Finger02_L'
names['Bip_New L Finger1']              = 'Finger1_L'
names['Bip_New L Finger11']             = 'Finger11_L'
names['Bip_New L Finger12']             = 'Finger12_L'
names['Bip_New L Finger2']              = 'Finger2_L'
names['Bip_New L Finger21']             = 'Finger21_L'
names['Bip_New L Finger22']             = 'Finger22_L'
names['Bip_New L Finger3']              = 'Finger3_L'
names['Bip_New L Finger31']             = 'Finger31_L'
names['Bip_New L Finger32']             = 'Finger32_L'
names['Bip_New L Finger4']              = 'Finger4_L'
names['Bip_New L Finger41']             = 'Finger41_L'
names['Bip_New L Finger42']             = 'Finger42_L'

names['Bip_New R Finger0']              = 'Finger0_R'
names['Bip_New R Finger01']             = 'Finger01_R'
names['Bip_New R Finger02']             = 'Finger02_R'
names['Bip_New R Finger1']              = 'Finger1_R'
names['Bip_New R Finger11']             = 'Finger11_R'
names['Bip_New R Finger12']             = 'Finger12_R'
names['Bip_New R Finger2']              = 'Finger2_R'
names['Bip_New R Finger21']             = 'Finger21_R'
names['Bip_New R Finger22']             = 'Finger22_R'
names['Bip_New R Finger3']              = 'Finger3_R'
names['Bip_New R Finger31']             = 'Finger31_R'
names['Bip_New R Finger32']             = 'Finger32_R'
names['Bip_New R Finger4']              = 'Finger4_R'
names['Bip_New R Finger41']             = 'Finger41_R'
names['Bip_New R Finger42']             = 'Finger42_R'

names['Bip_New L Thigh']                = 'Thigh_L'
names['Bip_New L Calf']                 = 'Calf_L'
names['Bip_New L Foot']                 = 'Foot_L'
names['Bip_New L Toe0']                 = 'Toe0_L'

names['Bip_New R Thigh']                = 'Thigh_R'
names['Bip_New R Calf']                 = 'Calf_R'
names['Bip_New R Foot']                 = 'Foot_R'
names['Bip_New R Toe0']                 = 'Toe0_R'

# Procedural bones/ helper bones
names['Bone_L Clavicle']                = 'Helper_Shoulder_L'      # NOTE: bone may have their names inverted
names['Bone L Soulder Twist']           = 'Helper_Shoulder_L'
names['Bone_L_Shoulder']                = 'Helper_Shoulder_L'
names['Bone L UpperArm']                = 'Helper_UpperArmTwist_L'
#names['Bone_UpperArm_Tw_L']    = "_UpperArmTwist_L"
names['Bone L UpperArm Twist']          = 'Helper_UpperArm_L'
names['Bip001_B_L Elbow']               = 'Helper_Elbow_L'
names['Bip001 L ForeTwist']             = 'Helper_Ulna_L'
names['Bip001 L ForeTwist1']            = 'Helper_Wrist_L'

names['Bone_R Clavicle']                = 'Helper_Shoulder_R'      # NOTE: bone may have their names inverted
names['Bone R Soulder Twist']           = 'Helper_Shoulder_R'
names['Bone_R_Shoulder']                = 'Helper_Shoulder_R'
names['Bone R UpperArm']                = 'Helper_UpperArmTwist_R'
#names['Bone_UpperArm_Tw_R']    = "_UpperArmTwist_R"
names['Bone R UpperArm Twist']          = 'Helper_UpperArm_R'
names['Bip001_B_R Elbow']               = 'Helper_Elbow_R'
names['Bip001 R ForeTwist']             = 'Helper_Ulna_R'
names['Bip001 R ForeTwist1']            = 'Helper_Wrist_R'

names['Bone_L_hip']                     = 'Helper_Hip_L'
names['Bone_L_Hip']                     = 'Helper_Hip_L'
names['Bip001 LThighTwist']             = 'Helper_Quadricep_L'
names['Bip001 L ThighTwist']            = 'Helper_Quadricep_L'
names['Bone_L_knee']                    = 'Helper_Knee_L'
names['Bip001_B_L Hip']                 = 'Helper_Glute_L'

names['Bone_R_hip']                     = 'Helper_Hip_R'
names['Bone_R_Hip']                     = 'Helper_Hip_R'
names['Bip001 RThighTwist']             = 'Helper_Quadricep_R'
names['Bip001 R ThighTwist']            = 'Helper_Quadricep_R'
names['Bone_R_knee']                    = 'Helper_Knee_R'
names['Bip001_B_R Hip']                 = 'Helper_Glute_R'

# Mostly, Jigglebones
# Hair-kind
names['Bip001 Xtra_hair']               = 'Hair'

names['Bone_Hair_B']                    = 'Hair_B'
names['Bone_Hair_F']                    = 'Hair_F'
names['Bone_Hair_FD']                   = 'Hair_FD'
names['Bone_Hair_FRD']                  = 'Hair_FRD'
names['Bone_Hair_LD']                   = 'Hair_LD'
names['Bone_Hair_M']                    = 'Hair_M'
names['Bone_Hair_R']                    = 'Hair_R'
names['Bone_Hair_RD']                   = 'Hair_RD'

names['BoneHair_00']                    = 'Hair_00'
names['BoneHair_01']                    = 'Hair_01'
names['BoneHair_02']                    = 'Hair_02'
names['BoneHair_03']                    = 'Hair_03'
names['BoneHair_04']                    = 'Hair_04'
names['BoneHair_05']                    = 'Hair_05'
names['BoneHair_06']                    = 'Hair_06'
names['BoneHair_07']                    = 'Hair_07'
names['BoneHair_08']                    = 'Hair_08'
names['BoneHair_09']                    = 'Hair_09'
names['BoneHair_10']                    = 'Hair_10'
names['BoneHair_11']                    = 'Hair_11'

names['BoneHair_012']                   = 'Hair_012'
names['BoneHair_013']                   = 'Hair_013'
names['BoneHair_014']                   = 'Hair_014'
names['BoneHair_015']                   = 'Hair_015'
names['BoneHair_016']                   = 'Hair_016'
names['BoneHair_017']                   = 'Hair_017'
names['BoneHair_018']                   = 'Hair_018'
names['BoneHair_019']                   = 'Hair_019'
names['BoneHair_020']                   = 'Hair_020'
names['BoneHair_021']                   = 'Hair_021'
names['BoneHair_022']                   = 'Hair_022'

names['Bone_HairRibbon_L_01']           = 'Hair_Ribbon_L_01'
names['Bone_HairRibbon_L_01']           = 'Hair_Ribbon_L_01'
names['Bone_HairRibbon_R_01']           = 'Hair_Ribbon_R_01'
names['Bone_HairRibbon_R_02']           = 'Hair_Ribbon_R_02'

names['Bone_PonyTail_M_01']             = 'PonyTail01_M'
names['Bone_PonyTail_M_02']             = 'PonyTail02_M'
names['Bone_PonyTail_M_03']             = 'PonyTail03_M'
names['Bone_PonyTail_M_04']             = 'PonyTail04_M'
names['Bone_PonyTail_M_05']             = 'PonyTail05_M'
names['Bone_PonyTail_L_01']             = 'PonyTail01_L'
names['Bone_PonyTail_L_02']             = 'PonyTail02_L'
names['Bone_PonyTail_R_01']             = 'PonyTail01_R'
names['Bone_PonyTail_R_02']             = 'PonyTail02_R'
names['Bone_PonyTail_U_01']             = 'PonyTail01_U'
names['Bone_PonyTail_U_02']             = 'PonyTail02_U'

# jiggles and additional bones per skin
names['Bone_L_Acc']                     = 'Acc_End_L'
names['Bip001 Xtra_L_Acc']              = 'Acc_L'
names['Bip001 Xtra_L_Acc02']            = 'Acc02_L'
names['Bip001 Xtra_L_Acc03']            = 'Acc03_L'
names['Bip001 Xtra_R_Acc_CosOpp']       = 'Acc_Cos_L'
names['Bip001 Xtra_R_Acc_CosOpp02']     = 'Acc_Cos02_L'
names['Bip001 Xtra_R_Acc_CosOpp03']     = 'Acc_Cos03_L'
names['Bip001 Xtra_R_Acc_CosOpp04']     = 'Acc_Cos04_L'

names['Bone_R_Acc']                     = 'Acc_End_R'
names['Bip001 Xtra_R_Acc']              = 'Acc_R'
names['Bip001 Xtra_R_Acc03']            = 'Acc03_R'
names['Bip001 Xtra_R_Acc02']            = 'Acc02_R'
names['Bip001 Xtra_R_Acc_Cos']          = 'Acc_Cos_R'
names['Bip001 Xtra_R_Acc_Cos02']        = 'Acc_Cos02_R'
names['Bip001 Xtra_R_Acc_Cos03']        = 'Acc_Cos03_R'
names['Bip001 Xtra_R_Acc_Cos04']        = 'Acc_Cos04_R'

# female characters have uncommon breast names
names['Bone_Bu_L']                      = 'Breast_L'        # actual jiggle
names['Bone_Bu_R']                      = 'Breast_R'        # actual jiggle
names['L_ BreastBone']                  = 'Breast_L'        # may also exist as jiggle
names['L_ BreastBone001']               = 'Breast_L'        # may also exist as jiggle
names['R_BreastBone']                   = 'Breast_R'        # may also exist as jiggle
names['R_BreastBone001']                = 'Breast_R'        # may also exist as jiggle

names['Point009']                       = 'Breast'          # dummy shit to attach objects in Unity
names['Point015']                       = 'Helper_Breast'   # center control
names['Point007']                       = 'Helper_Breast_L' # left procedural fixup
names['Point010']                       = 'Helper_Breast_R' # right procedural fixup

# clothes jiggles
names['RopeBone_L_0']                   = 'Rope0_L'
names['RopeBone_L_1']                   = 'Rope1_L'
names['RopeBone_L_2']                   = 'Rope2_L'
names['RopeBone_R_0']                   = 'Rope0_R'
names['RopeBone_R_1']                   = 'Rope1_R'
names['RopeBone_R_2']                   = 'Rope2_R'

names['Bip001 Xtra_RB_Skt03']           = 'B_Skt03_R'
names['Bip001 Xtra_RB_Skt02']           = 'B_Skt02_R'
names['Bip001 Xtra_LB_Skt02']           = 'B_Skt02_L'
names['Bip001 Xtra_RB_Skt']             = 'B_Skt_R'
names['Bip001 Xtra_RF_Skt']             = 'F_Skt_R'
names['Bip001 Xtra_LF_Skt04']           = 'F_Skt04_L'
names['Bip001 Xtra_RF_Skt02']           = 'F_Skt02_R'
names['Bip001 Xtra_LF_Skt']             = 'F_Skt_L'
names['Bip001 Xtra_LB_Skt05']           = 'B_Skt05_L'
names['Bip001 Xtra_RB_Skt05']           = 'B_Skt05_R'
names['Bip001 Xtra_LF_Skt03']           = 'F_Skt03_L'
names['Bip001 Xtra_LF_Skt02']           = 'F_Skt02_L'
names['Bip001 Xtra_LB_Skt03']           = 'B_Skt03_L'
names['Bip001 Xtra_LB_Skt04']           = 'B_Skt04_L'
names['Bip001 Xtra_RF_Skt03']           = 'F_Skt03_R'
names['Bip001 Xtra_RB_Skt04']           = 'B_Skt04_R'
names['Bip001 Xtra_RF_Skt04']           = 'F_Skt04_R'
names['Bip001 Xtra_LB_Skt']             = 'B_Skt_L'

names['skirt_L_01']                     = 'Skirt_L_01'
names['skirt_L_02']                     = 'Skirt_L_02'
names['skirt_LB_01']                    = 'Skirt_LB_01'
names['skirt_LB_02']                    = 'Skirt_LB_02'
names['skirt_LF_01']                    = 'Skirt_LF_01'
names['skirt_LF_02']                    = 'Skirt_LF_02'

names['skirt_R_01']                     = 'Skirt_R_01'
names['skirt_R_02']                     = 'Skirt_R_02'
names['skirt_RB_01']                    = 'Skirt_RB_01'
names['skirt_RB_02']                    = 'Skirt_RB_02'
names['skirt_RF_01']                    = 'Skirt_RF_01'
names['skirt_RF_02']                    = 'Skirt_RF_02'
names['skirt_RF_03']                    = 'Skirt_RF_03'
names['skirt_RF_04']                    = 'Skirt_RF_04'

names['Bone_Sleeve_L_00']               = 'Sleeve00_L'
names['Bone_Sleeve_L_07']               = 'Sleeve07_L'
names['Bone_Sleeve_L_08']               = 'Sleeve08_L'
names['Bone_Sleeve_L_01']               = 'Sleeve01_L'
names['Bone_Sleeve_L_03']               = 'Sleeve03_L'
names['Bone_Sleeve_L_04']               = 'Sleeve04_L'
names['Bone_Sleeve_L_02']               = 'Sleeve02_L'
names['Bone_Sleeve_L_05']               = 'Sleeve05_L'
names['Bone_Sleeve_L_06']               = 'Sleeve06_L'

names['Bone_Sleeve_R_00']               = 'Sleeve00_R'
names['Bone_Sleeve_R_07']               = 'Sleeve07_R'
names['Bone_Sleeve_R_08']               = 'Sleeve08_R'
names['Bone_Sleeve_R_01']               = 'Sleeve01_R'
names['Bone_Sleeve_R_03']               = 'Sleeve03_R'
names['Bone_Sleeve_R_04']               = 'Sleeve04_R'
names['Bone_Sleeve_R_02']               = 'Sleeve02_R'
names['Bone_Sleeve_R_05']               = 'Sleeve05_R'
names['Bone_Sleeve_R_06']               = 'Sleeve06_R'

# mostly/likely props
names['umb_00']                         = 'Umb_00'
names['umb_01']                         = 'Umb_01'
names['umbrella_00']                    = 'Umbrella_00'
names['umbrella_01']                    = 'Umbrella_01'
names['umbrella_02']                    = 'Umbrella_02'
names['umbrella_03']                    = 'Umbrella_03'
names['umbrella_04']                    = 'Umbrella_04'
names['umbrella_05']                    = 'Umbrella_05'
names['umbrella_06']                    = 'Umbrella_06'
names['umbrella_07']                    = 'Umbrella_07'
names['umbrella_08']                    = 'Umbrella_08'
names['umbrella_09']                    = 'Umbrella_09'
names['umbrella_10']                    = 'Umbrella_10'
names['umbrella_11']                    = 'Umbrella_11'
names['umbrella_12']                    = 'Umbrella_12'
names['umbrella_13']                    = 'Umbrella_13'
names['umbrella_14']                    = 'Umbrella_14'
names['umbrella_15']                    = 'Umbrella_15'
names['umbrella_16']                    = 'Umbrella_16'
names['umbrella_17']                    = 'Umbrella_17'
names['umbrella_18']                    = 'Umbrella_18'
names['umbrella_19']                    = 'Umbrella_19'

# unknow bones
#names['Bone001']                        = 'Bone001'
#names['Bone002']                        = 'Bone002'
#names['Bone004']                        = 'Bone004'
#names['Bone006']                        = 'Bone006'
#names['Bone008']                        = 'Bone008'
#names['Bone009']                        = 'Bone009'
#names['Bone012']                        = 'Bone012'
#names['Bone014']                        = 'Bone014'

# dummy reference animation attachments
names['Bone_L_Eye']                     = 'lefteye'
names['Bone_R_Eye']                     = 'righteye'
names['Bip001 Xtra_Eye_Ctrl']           = 'Eye_Ctrl'

names['ViewPoint001']                   = 'forward'
names['ViewPoint']                      = 'forward'

names['L_Thruster']                     = 'Thruster_L'
names['R_Thruster']                     = 'Thruster_R'

names['L WeaponPoint']                  = 'WeaponPoint_L'
names['R WeaponPoint']                  = 'WeaponPoint_R'

names['L WeaponPoint001']               = 'WeaponPoint_L'
names['R WeaponPoint001']               = 'WeaponPoint_R'

names['L BusterPoint']                  = 'BusterPoint_L'
names['R BusterPoint']                  = 'BusterPoint_R'

names['L BusterPoint001']               = 'BusterPoint_L'
names['R BusterPoint001']               = 'BusterPoint_R'

names['Bip_General Footsteps']          = 'Footsteps'
names['Bip_New Footsteps']              = 'Footsteps'
names['L']                              = 'L'
names['L001']                           = 'L'
names['R']                              = 'R'
names['R001']                           = 'R'

names['L_Thruster001']                  = 'Thruster001_L'
names['R_Thruster001']                  = 'Thruster001_R'

