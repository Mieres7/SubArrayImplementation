# List of valid array assemblies supported by this package
VALID_AA_MID = [
    "AA4",
    "AA*",
    "AA2",
    "AA1",
    "AA0.5",
    "custom",
]

VALID_AA_LOW = [
    "AA4",
    "AA*",
    "AA2",
    "AA1",
    "AA0.5",
    "custom",
]

# AA0.5 will have 4 stations.
# Taken from ECP-240008
LOW_AA05 = "S8-1,S8-6,S9-2,S10-3"

# AA1 will have 18 stations. The station list was taken from the LOW Roll-Out Plan
# document (SKA-TEL-AIV-4410001 Revision 10)
# Low Roll-Out Plan revision 10 has been updated to incorporate changes
# introduced via ECP-240120. This ECP reduces the number of AA1 stations to 16.
LOW_AA1 = (
    "S8-1,S8-2,S8-3,S8-4,S8-5,S8-6,"
    + "S9-1,S9-2,S9-3,S9-4,"
    + "S10-1,S10-2,S10-3,S10-4,S10-5,S10-6"
)

# LOW AA2 will have 64 stations.
# The station list was taken from the LOW Roll-Out Plan
# document (SKA-TEL-AIV-4410001 Revision 10)
# Low Roll-Out Plan revision 10 has been updated to incorporate changes
# introduced via ECP-240120.
LOW_AA2 = (
    "S8-1,S8-2,S8-3,S8-4,S8-5,S8-6,"
    + "S9-1,S9-2,S9-3,S9-4,"
    + "S10-1,S10-2,S10-3,S10-4,S10-5,S10-6,"
    + "S16-1,S16-2,S16-3,S16-4,"
    + "N1-1,N1-2,"
    + "E1-1,E1-2,"
    + "66,111,22,69,80,30,78,91,23,36,108,52,193,16,98,56,146,70,200,57,132,62,"
    + "90,73,183,176,17,88,32,31,33,89,59,165,8,158,144,72,4,167"
)

# AA* will have 307 stations. The station list was taken from the
# LOW Roll-Out Plan document (SKA-TEL-AIV-4410001 Revision 10)
# + station 47 which will be added to the roll-out plan in the next release
#
# Low Roll-Out Plan revision 10 has been updated to incorporate changes
# introduced via ECP-240120
LOW_AAstar = (
    "S1-1,S1-2,"
    + "S2-1,S2-2,S2-3,"
    + "S3-1,S3-2,"
    + "S4-1,S4-2,S4-3,"
    + "S8-1,S8-2,S8-3,S8-4,S8-5,S8-6,"
    + "S9-1,S9-2,S9-3,S9-4,"
    + "S10-1,S10-2,S10-3,S10-4,S10-5,S10-6,"
    + "S13-1,S13-2,S13-3,S13-4,"
    + "S15-1,S15-2,S15-3,S15-4,"
    + "S16-1,S16-2,S16-3,S16-4,"
    + "N1-1,N1-2,"
    + "N2-1,N2-2,N2-3,"
    + "N3-1,N3-2,N3-3,"
    + "N4-1,N4-2,N4-3,"
    + "N8-1,N8-2,N8-3,N8-4,"
    + "N9-1,N9-2,N9-3,N9-4,"
    + "N10-1,N10-2,N10-3,N10-4,"
    + "N13-1,N13-2,N13-3,N13-4,"
    + "N15-1,N15-2,N15-3,N15-4,"
    + "N16-1,N16-2,N16-3,N16-4,"
    + "E1-1,E1-2,"
    + "E2-1,E2-2,E2-3,"
    + "E3-1,E3-2,E3-3,"
    + "E4-1,E4-2,E4-3,"
    + "E8-1,E8-2,E8-3,E8-4,"
    + "E9-1,E9-2,E9-3,E9-4,"
    + "E10-1,E10-2,E10-3,E10-4,"
    + "E13-1,E13-2,E13-3,E13-4,"
    + "E15-1,E15-2,E15-3,E15-4,"
    + "E16-1,E16-2,E16-3,E16-4,"
    + "66, 111, 22, 69, 80, 30, 78, 91, 23, 36, 108, 52, 193, 16, 98, 56, "
    + "146, 70, 200, 57, 132, 62, 90, 73, 183, 176, 17, 88, 32, 31, 33, 89, "
    + "59, 165, 8, 158, 144, 72, 4, 167, 14, 185, 142, 19, 224, 7, 160, 74, "
    + "42, 171, 79, 96, 27, 75, 85, 212, 15, 63, 205, 24, 29, 25, 112, 187, "
    + "84, 1, 120, 175, 44, 38, 67, 54, 155, 49, 170, 87, 216, 105, 35, 156, "
    + "121, 86, 58, 150, 60, 143, 68, 151, 18, 45, 100, 76, 195, 107, 34, 172, "
    + "20, 64, 191, 115, 2, 125, 48, 71, 61, 130, 55, 202, 223, 140, 37, 41, 46, "
    + "139, 213, 104, 9, 99, 13, 192, 114, 204, 21, 12, 147, 82, 103, 138, 106, "
    + "11, 119, 6, 194, 5, 93, 168, 28, 197, 154, 26, 92, 110, 77, 50, 10, 53, "
    + "95, 166, 40, 128, 162, 113, 222, 129, 214, 102, 65, 109, 97, 123, 141, "
    + "39, 83, 148, 198, 81, 3, 135, 51, 145, 207, 149, 137, 43, 163, 101, 181, "
    + "180, 117, 206, 126, 177, 124, 133, 208, 190, 153, 164, 173, 219, 201, 184, "
    + "217, 203, 186, 199, 161, 179, "
    + "47"
)

# MID roll-out plan extracted from the
# SKA1 Mid Staged Deliver Plan (SKA-TEL-SKO-0001827 revision 02)
# with the following modifications:
# - Chose SKA026 and SKA111 as the possible locations for the two unknown MK+ dishes
# - Since these two dishes are part of AA2, SKA097 and SKA051 have been brought forward
#   from AA4.

# List of MID dishes in AA0.5
MID_AA05 = "SKA063,SKA001,SKA100,SKA036"

# List of MID dishes in AA1
MID_AA1 = MID_AA05 + "," + "SKA046,SKA048,SKA077,SKA081"

# List of MeerKAT antennas
MID_MKAT = (
    "M000,M001,M002,M003,M004,M005,M006,M007,M008,M009,M010,M011,M012,M013,"
    + "M014,M015,M016,M017,M018,M019,M020,M021,M022,M023,M024,M025,M026,M027,"
    + "M028,M029,M030,M031,M032,M033,M034,M035,M036,M037,M038,M039,M040,M041,"
    + "M042,M043,M044,M045,M046,M047,M048,M049,M050,M051,M052,M053,M054,M055,"
    + "M056,M057,M058,M059,M060,M061,M062,M063"
)

# MeerKAT+ antenna list
MID_MKAT_PLUS = (
    # 14 confirmed locations
    "SKA017,SKA018,SKA020,SKA023,"
    + "SKA060,SKA105,SKA107,SKA110,"
    + "SKA115,SKA116,SKA117,SKA118,"
    + "SKA119,SKA121,"
    # and 2 locations TBC
    + "SKA026,SKA111"
)

# MID AA2 will have 64 antennas
# Roll out plan has been modified to accommodate the three TBC MK+ dishes
MID_AA2 = (
    # Batch 1
    MID_AA1
    + ","
    + "SKA015,SKA025,SKA037,SKA008,"
    + "SKA013,SKA014,SKA016,SKA019,"
    + "SKA027,SKA028,SKA030,SKA032,"
    + "SKA033,SKA035,SKA038,SKA039,"
    + "SKA040,SKA041,SKA042,SKA043,"
    + "SKA024,SKA045,SKA049,SKA050,"
    + "SKA031,SKA034,SKA055,"  # SKA026 moved to MK+
    + "SKA061,SKA067,SKA068,SKA070,"
    + "SKA075,SKA079,SKA082,SKA083,"  # 083 replace 060
    + "SKA089,SKA091,SKA092,"  # SKA111 moved to MK+
    + "SKA095,SKA096,SKA114,SKA098,"
    + "SKA099,SKA101,SKA102,SKA103,"
    + "SKA104,SKA106,SKA108,SKA109,"
    + "SKA113,SKA123,SKA125,SKA126,"
    # Two TBC dishes to replace SKA026 and SKA111
    + "SKA097,SKA051"
)

# MID AA* will have 144 antennas (64 AA2 antennas + 64 MeerKAT + 16 MeerKAT+)
MID_AAstar = MID_AA2 + "," + MID_MKAT_PLUS + "," + MID_MKAT
