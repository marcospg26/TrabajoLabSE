/**********************************************************************/
/*   ____  ____                                                       */
/*  /   /\/   /                                                       */
/* /___/  \  /                                                        */
/* \   \   \/                                                         */
/*  \   \        Copyright (c) 2003-2020 Xilinx, Inc.                 */
/*  /   /        All Right Reserved.                                  */
/* /---/   /\                                                         */
/* \   \  /  \                                                        */
/*  \___\/\___\                                                       */
/**********************************************************************/

#if defined(_WIN32)
 #include "stdio.h"
 #define IKI_DLLESPEC __declspec(dllimport)
#else
 #define IKI_DLLESPEC
#endif
#include "iki.h"
#include <string.h>
#include <math.h>
#ifdef __GNUC__
#include <stdlib.h>
#else
#include <malloc.h>
#define alloca _alloca
#endif
/**********************************************************************/
/*   ____  ____                                                       */
/*  /   /\/   /                                                       */
/* /___/  \  /                                                        */
/* \   \   \/                                                         */
/*  \   \        Copyright (c) 2003-2020 Xilinx, Inc.                 */
/*  /   /        All Right Reserved.                                  */
/* /---/   /\                                                         */
/* \   \  /  \                                                        */
/*  \___\/\___\                                                       */
/**********************************************************************/

#if defined(_WIN32)
 #include "stdio.h"
 #define IKI_DLLESPEC __declspec(dllimport)
#else
 #define IKI_DLLESPEC
#endif
#include "iki.h"
#include <string.h>
#include <math.h>
#ifdef __GNUC__
#include <stdlib.h>
#else
#include <malloc.h>
#define alloca _alloca
#endif
typedef void (*funcp)(char *, char *);
extern int main(int, char**);
IKI_DLLESPEC extern void execute_1651(char*, char *);
IKI_DLLESPEC extern void execute_1652(char*, char *);
IKI_DLLESPEC extern void execute_1640(char*, char *);
IKI_DLLESPEC extern void execute_1641(char*, char *);
IKI_DLLESPEC extern void execute_1642(char*, char *);
IKI_DLLESPEC extern void execute_1643(char*, char *);
IKI_DLLESPEC extern void execute_1644(char*, char *);
IKI_DLLESPEC extern void execute_57(char*, char *);
IKI_DLLESPEC extern void execute_58(char*, char *);
IKI_DLLESPEC extern void execute_59(char*, char *);
IKI_DLLESPEC extern void execute_60(char*, char *);
IKI_DLLESPEC extern void execute_63(char*, char *);
IKI_DLLESPEC extern void execute_64(char*, char *);
IKI_DLLESPEC extern void execute_65(char*, char *);
IKI_DLLESPEC extern void execute_66(char*, char *);
IKI_DLLESPEC extern void execute_67(char*, char *);
IKI_DLLESPEC extern void execute_68(char*, char *);
IKI_DLLESPEC extern void execute_73(char*, char *);
IKI_DLLESPEC extern void execute_74(char*, char *);
IKI_DLLESPEC extern void execute_75(char*, char *);
IKI_DLLESPEC extern void execute_76(char*, char *);
IKI_DLLESPEC extern void execute_79(char*, char *);
IKI_DLLESPEC extern void execute_86(char*, char *);
IKI_DLLESPEC extern void execute_87(char*, char *);
IKI_DLLESPEC extern void execute_88(char*, char *);
IKI_DLLESPEC extern void execute_89(char*, char *);
IKI_DLLESPEC extern void execute_90(char*, char *);
IKI_DLLESPEC extern void execute_91(char*, char *);
IKI_DLLESPEC extern void execute_42(char*, char *);
IKI_DLLESPEC extern void execute_56(char*, char *);
IKI_DLLESPEC extern void execute_62(char*, char *);
IKI_DLLESPEC extern void execute_70(char*, char *);
IKI_DLLESPEC extern void execute_72(char*, char *);
IKI_DLLESPEC extern void execute_81(char*, char *);
IKI_DLLESPEC extern void execute_889(char*, char *);
IKI_DLLESPEC extern void execute_890(char*, char *);
IKI_DLLESPEC extern void execute_892(char*, char *);
IKI_DLLESPEC extern void execute_1495(char*, char *);
IKI_DLLESPEC extern void execute_1496(char*, char *);
IKI_DLLESPEC extern void execute_1498(char*, char *);
IKI_DLLESPEC extern void execute_1620(char*, char *);
IKI_DLLESPEC extern void execute_1621(char*, char *);
IKI_DLLESPEC extern void execute_1622(char*, char *);
IKI_DLLESPEC extern void execute_1623(char*, char *);
IKI_DLLESPEC extern void execute_1624(char*, char *);
IKI_DLLESPEC extern void execute_1625(char*, char *);
IKI_DLLESPEC extern void execute_1626(char*, char *);
IKI_DLLESPEC extern void execute_1627(char*, char *);
IKI_DLLESPEC extern void execute_1628(char*, char *);
IKI_DLLESPEC extern void execute_1629(char*, char *);
IKI_DLLESPEC extern void execute_1630(char*, char *);
IKI_DLLESPEC extern void execute_1639(char*, char *);
IKI_DLLESPEC extern void execute_1501(char*, char *);
IKI_DLLESPEC extern void execute_1502(char*, char *);
IKI_DLLESPEC extern void execute_1505(char*, char *);
IKI_DLLESPEC extern void execute_1646(char*, char *);
IKI_DLLESPEC extern void execute_1647(char*, char *);
IKI_DLLESPEC extern void transaction_0(char*, char*, unsigned, unsigned, unsigned);
IKI_DLLESPEC extern void vhdl_transfunc_eventcallback(char*, char*, unsigned, unsigned, unsigned, char *);
funcp funcTab[59] = {(funcp)execute_1651, (funcp)execute_1652, (funcp)execute_1640, (funcp)execute_1641, (funcp)execute_1642, (funcp)execute_1643, (funcp)execute_1644, (funcp)execute_57, (funcp)execute_58, (funcp)execute_59, (funcp)execute_60, (funcp)execute_63, (funcp)execute_64, (funcp)execute_65, (funcp)execute_66, (funcp)execute_67, (funcp)execute_68, (funcp)execute_73, (funcp)execute_74, (funcp)execute_75, (funcp)execute_76, (funcp)execute_79, (funcp)execute_86, (funcp)execute_87, (funcp)execute_88, (funcp)execute_89, (funcp)execute_90, (funcp)execute_91, (funcp)execute_42, (funcp)execute_56, (funcp)execute_62, (funcp)execute_70, (funcp)execute_72, (funcp)execute_81, (funcp)execute_889, (funcp)execute_890, (funcp)execute_892, (funcp)execute_1495, (funcp)execute_1496, (funcp)execute_1498, (funcp)execute_1620, (funcp)execute_1621, (funcp)execute_1622, (funcp)execute_1623, (funcp)execute_1624, (funcp)execute_1625, (funcp)execute_1626, (funcp)execute_1627, (funcp)execute_1628, (funcp)execute_1629, (funcp)execute_1630, (funcp)execute_1639, (funcp)execute_1501, (funcp)execute_1502, (funcp)execute_1505, (funcp)execute_1646, (funcp)execute_1647, (funcp)transaction_0, (funcp)vhdl_transfunc_eventcallback};
const int NumRelocateId= 59;

void relocate(char *dp)
{
	iki_relocate(dp, "xsim.dir/image_test_behav/xsim.reloc",  (void **)funcTab, 59);
	iki_vhdl_file_variable_register(dp + 8675088);
	iki_vhdl_file_variable_register(dp + 8675144);


	/*Populate the transaction function pointer field in the whole net structure */
}

void sensitize(char *dp)
{
	iki_sensitize(dp, "xsim.dir/image_test_behav/xsim.reloc");
}

	// Initialize Verilog nets in mixed simulation, for the cases when the value at time 0 should be propagated from the mixed language Vhdl net

void simulate(char *dp)
{
		iki_schedule_processes_at_time_zero(dp, "xsim.dir/image_test_behav/xsim.reloc");

	iki_execute_processes();

	// Schedule resolution functions for the multiply driven Verilog nets that have strength
	// Schedule transaction functions for the singly driven Verilog nets that have strength

}
#include "iki_bridge.h"
void relocate(char *);

void sensitize(char *);

void simulate(char *);

extern SYSTEMCLIB_IMP_DLLSPEC void local_register_implicit_channel(int, char*);
extern SYSTEMCLIB_IMP_DLLSPEC int xsim_argc_copy ;
extern SYSTEMCLIB_IMP_DLLSPEC char** xsim_argv_copy ;

int main(int argc, char **argv)
{
    iki_heap_initialize("ms", "isimmm", 0, 2147483648) ;
    iki_set_xsimdir_location_if_remapped(argc, argv)  ;
    iki_set_sv_type_file_path_name("xsim.dir/image_test_behav/xsim.svtype");
    iki_set_crvs_dump_file_path_name("xsim.dir/image_test_behav/xsim.crvsdump");
    void* design_handle = iki_create_design("xsim.dir/image_test_behav/xsim.mem", (void *)relocate, (void *)sensitize, (void *)simulate, (void*)0, 0, isimBridge_getWdbWriter(), 0, argc, argv);
     iki_set_rc_trial_count(100);
    (void) design_handle;
    return iki_simulate_design();
}
