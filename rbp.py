from robotButlerPal import vernacular, comm_style, learning_style, teaching_style
# vernacular module will have the called functions listed in vernacular();
# comm_style module will have the called functions listed in comm_style();



# user-related functions i want to write:

def vernacular(user_vernacular):
	vernaculars_dict = {
		east_coast = east_coast_vernacular(),
		cali = cali_vernacular(),
		dc = dc_vernacular(),
		midwest = midwest_vernacular(),
		texas = texas_vernacular(),
		northwest = northwest_vernacular(),
		middle_america = middle_america_vernacular()
	}
	if user_vernacular in vernaculars_dict.keys():
		return vernacular_dict['user_vernacular']
		# whatever vernacular uses, use that vernacular with the user to make rbp easier to get used to.
		# later, consider allowing the user to choose which vernacular (s)he prefers rbp to use.

def comm_style(user_comm_style[, user_comm_style_1][, user_comm_style_2][, user_comm_style_3][, user_comm_style_4][, user_comm_style_5]):
	communication_styles_dict = { 
	# might aka management_style()/_dict {};
	# what would we call someone who has more than 5 comm styles? 'chameleon'?
		passive = passive_comm_style(),
		aggressive = aggressive_comm_style(),
		passive_aggressive = passive_aggressive_comm_style(),
		assertive = assertive_comm_style(),
		submissive = submissive_comm_style(),
		manipulative = manipulative_comm_style(),
		# the following 8 styles source='https://www.educba.com/different-methods-of-communication/'
		verbal = verbal_comm_style(),
		non_verbal = non_verbal_comm_style(),
		physical_non_verbal = physical_non_verbal_comm_style(),
		written = written_comm_style(),
		visual = visual_comm_style(),
		paralanguage = paralanguage_comm_style(),
		oral = oral_comm_style(),
		face_to_face = face_to_face_comm_style(),
		# the above 8 styles source='https://www.educba.com/different-methods-of-communication/'
		narcissistic = narcissistic_comm_style([grandiose_self_importance][, fantasies_of_success_power][, special_unique][, admiration][, entitlement][, lack_of_empathy][, envy][, arrogance]),
			# narcissistic's 9 args are based on DSM V diagnosis criteria source='http://www.psi.uba.ar/academica/carrerasdegrado/psicologia/sitios_catedras/practicas_profesionales/820_clinica_tr_personalidad_psicosis/material/dsm.pdf'
		# the following are examples of various personalities/compound styles
		dark_and_broody = passive and non_verbal and physical_non_verbal and paralanguage,
		bubbly = passive and verbal and oral and face_to_face,
		dictator = aggressive and assertive and manipulative and verbal and physical_non_verbal and oral and face_to_face and paralanguage,
		dominant = assertive and manipulative and non_verbal and physical_non_verbal and face_to_face,
		funny_guy = passive and passive_aggressive and assertive and verbal and oral and face_to_face
	}
	if user_comm_style in comm_style_dict.keys():
		return comm_style_dict['user_comm_style']

def learning_style(user_learning_style):
	learning_style_dict = {
		reader = reader_learning_style(),
		listener = listener_learning_style(),
		youtube = youtube_learning_style(),
		apprentice = apprentice_learning_style(),
		self_taught = self_taught_learning_style(),
		coachable = coachable_learning_style()
	}
	if user_learning_style in learning_style_dict.keys:
		return learning_style_dict['user_learning_style']


# =============================================
# = = = = = = = = = = = = = = = = = = = = = = =
# =============================================
# rbp-related functions i want to write:
def teaching_style([user_need]):
	teaching_style_dict = {
		tutor = tutor_teaching_style(),
		genius = genius_teaching_style(),
		motivation = motivational_teaching_style(),
		strict = strict_teaching_style(),
		demanding_expectant = demanding_expectant_teaching_style(),
	}
	if user_need in teaching_style_dict.keys:
		return teaching_style_dict['user_need']

