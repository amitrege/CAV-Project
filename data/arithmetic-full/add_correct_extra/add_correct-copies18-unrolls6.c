
#include <stdio.h>

int main(void) { 
	int It = 364 ; 

	int WEcB9M ;
	WEcB9M = 639 ;


	if ( WEcB9M > 1 ) { 

		It += It ;

		WEcB9M = WEcB9M - 1 ;

	
		if ( WEcB9M > 1 ) { 

			It = It + It ;

			WEcB9M -- ; 

		
			if ( WEcB9M > 1 ) { 

				It += It ;

				WEcB9M -- ; 

			
				if ( WEcB9M > 1 ) { 

					It = It + It ;

					WEcB9M -- ; 

				
					if ( WEcB9M > 1 ) { 

						It = It + It ;

						WEcB9M -- ; 

					
						if ( WEcB9M > 1 ) { 

							It += It ;

							WEcB9M = WEcB9M - 1 ;

						
							while ( WEcB9M > 1 ) { 

								It += It ;

								WEcB9M -- ; 

							}

						}

					}

				}

			}

		}

	}

	printf ( " %d " , It ) ;

} 
