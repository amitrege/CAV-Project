
#include <stdio.h>

int main(void) { 
	int bTnc = 531 ; 

	int KHDI ;
	KHDI = 831 ;


	if ( KHDI > 1 ) { 

		bTnc = bTnc + bTnc ;

		KHDI -- ; 

	
		if ( KHDI > 1 ) { 

			bTnc = bTnc + bTnc ;

			KHDI = KHDI - 1 ;

		
			if ( KHDI > 1 ) { 

				bTnc += bTnc ;

				KHDI = KHDI - 1 ;

			
				if ( KHDI > 1 ) { 

					bTnc = bTnc + bTnc ;

					KHDI = KHDI - 1 ;

				
					if ( KHDI > 1 ) { 

						bTnc = bTnc + bTnc ;

						KHDI = KHDI - 1 ;

					
						if ( KHDI > 1 ) { 

							bTnc += bTnc ;

							KHDI -- ; 

						
							while ( KHDI > 1 ) { 

								bTnc = bTnc + bTnc ;

								KHDI -- ; 

							}

						}

					}

				}

			}

		}

	}

	printf ( " %d " , bTnc ) ;

} 
