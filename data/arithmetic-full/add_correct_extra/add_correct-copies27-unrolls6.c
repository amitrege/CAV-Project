
#include <stdio.h>

int main(void) { 

	int nsnuNr1PTo ;
	nsnuNr1PTo = 211 ;

	int DVDtqqo ;
	DVDtqqo = 415 ;


	if ( DVDtqqo > 1 ) { 

		nsnuNr1PTo += nsnuNr1PTo ;

		DVDtqqo -- ; 

	
		if ( DVDtqqo > 1 ) { 

			nsnuNr1PTo = nsnuNr1PTo + nsnuNr1PTo ;

			DVDtqqo = DVDtqqo - 1 ;

		
			if ( DVDtqqo > 1 ) { 

				nsnuNr1PTo += nsnuNr1PTo ;

				DVDtqqo = DVDtqqo - 1 ;

			
				if ( DVDtqqo > 1 ) { 

					nsnuNr1PTo = nsnuNr1PTo + nsnuNr1PTo ;

					DVDtqqo = DVDtqqo - 1 ;

				
					if ( DVDtqqo > 1 ) { 

						nsnuNr1PTo += nsnuNr1PTo ;

						DVDtqqo = DVDtqqo - 1 ;

					
						if ( DVDtqqo > 1 ) { 

							nsnuNr1PTo += nsnuNr1PTo ;

							DVDtqqo = DVDtqqo - 1 ;

						
							while ( DVDtqqo > 1 ) { 

								nsnuNr1PTo = nsnuNr1PTo + nsnuNr1PTo ;

								DVDtqqo = DVDtqqo - 1 ;

							}

						}

					}

				}

			}

		}

	}

	printf ( " %d " , nsnuNr1PTo ) ;


	return 0 ; 
} 
