
#include <stdio.h>

int main(void) { 

	int eJG1 ;
	eJG1 = 709 ;

	int ke ;
	ke = 539 ;


	if ( ke > 1 ) { 

		eJG1 += eJG1 ;

		ke = ke - 1 ;

	
		if ( ke > 1 ) { 

			eJG1 += eJG1 ;

			ke -- ; 

		
			if ( ke > 1 ) { 

				eJG1 = eJG1 + eJG1 ;

				ke -- ; 

			
				if ( ke > 1 ) { 

					eJG1 += eJG1 ;

					ke -- ; 

				
					if ( ke > 1 ) { 

						eJG1 += eJG1 ;

						ke = ke - 1 ;

					
						if ( ke > 1 ) { 

							eJG1 += eJG1 ;

							ke = ke - 1 ;

						
							while ( ke > 1 ) { 

								eJG1 = eJG1 + eJG1 ;

								ke = ke - 1 ;

							}

						}

					}

				}

			}

		}

	}

	printf ( " %d " , eJG1 ) ;

} 
