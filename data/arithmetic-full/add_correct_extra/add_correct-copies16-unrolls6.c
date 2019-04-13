
#include <stdio.h>

int main(void) { 
	int YMw1X = 848 ; 
	int L = 305 ; 


	if ( L > 1 ) { 

		YMw1X = YMw1X + YMw1X ;

		L -- ; 

	
		if ( L > 1 ) { 

			YMw1X += YMw1X ;

			L -- ; 

		
			if ( L > 1 ) { 

				YMw1X += YMw1X ;

				L = L - 1 ;

			
				if ( L > 1 ) { 

					YMw1X += YMw1X ;

					L -- ; 

				
					if ( L > 1 ) { 

						YMw1X = YMw1X + YMw1X ;

						L = L - 1 ;

					
						if ( L > 1 ) { 

							YMw1X = YMw1X + YMw1X ;

							L = L - 1 ;

						
							while ( L > 1 ) { 

								YMw1X += YMw1X ;

								L = L - 1 ;

							}

						}

					}

				}

			}

		}

	}

	printf ( " %d " , YMw1X ) ;


	return 0 ; 
} 
