;Rajan Patel
;CMSC 471 Section 1
;Homework 1
;Due: 9/15/15 12:59 PM


;Returns the number that is two less than its integer argument
;Check for non-numeric/non int inputs
(defun lesstwo (n)
	(if (not (integerp n))
		(progn
			(error "Not a integer number.")
			;(return-from lesstwo nil)
			
			)
	(- n 2 )
	)
)


;Returns the factorial argument of n
;check for non-numeric inputs
;test for 0
;need to test for negative

;Returns the factorial of and integer number
;Handles non-integer inputs, negative inputs, and zero
(defun fact (n)
	(if (and (integerp n) (>= n 0))
		(if ( = n 0 )
			1
			( * (fact( - n 1)) n )

		)
		(progn
			(print "Please enter an integer.")
			nil
		)	

		
	)

)

;uses mapcar to apply a function to all element in a list
;if the element is a list posint1 is called on it
(defun posint1 (l)

	; (mapcan (lambda(x) (if(and (integerp x) (> x 0)))  )l)

	; 	(list x)

	; (if(and (not (= x nil) (not (atom x))) ) 
	; 	posint1(l)
	; )
	(setq l ( flatten-list l ) ) ;basically handles cons

	   (remove-if #'null ( mapcar ( if ( integerp x )
	      ( if ( > x 0 )
	         x
	      ) l ) )


		)
)


;uses a looping macro to loop through the list
(defun posint2 (l)
	;basically handles cons
	(setq l ( flatten-list l ) ) 
	;loops for each element x in l
	(loop for x in l 

		when (integep x)

		when (> x 0)

		collect x
	)
)

;recurvsive function to 
(defun posint3 (l)
	(cond 
		;checks if list is empty	
      ((endp l)
        nil
      )
      ((integerp (car l) )
         (progn 

            (if ( > (car l) 0)
               (cons (car l) ( posint3 (cdr l))) 
               (posint3 ( cdr l ))
            )
         )
      )
      ((listp (car l)
      		;again used flatten-list instead of the (car+cdr workaround)
         ( cons (posint3 (flatten-list (car l))) ( posint3 ( cdr l )))
      )
      (t nil) 
   )
)
	)


; (listp '(1 2)) == T
; (listp '(1 . 2)) == T
; (consp '(1 2)) == T
; (consp '(1 . 2)) == T

	
;Returns the third element of the list
;DOES NOT CHECK FOR CONS
(defun my-third (l)
	(if(listp l)
		;(if (consp l)
			;(print "Incorrect input.")
			(car (cdr (cdr l)))
		;)
		
		(progn
			(print "Incorrect input. Please enter a list of 3 or greater.")
			nil
		)

	  )
) 



;flattens a deeply nested list of atoms
;need to check for cons
(defun flatten-list (l )
	(if (null l )
		nil
	(progn
	(if (listp (first l ))
		(append (flatten-list (car l )) (flatten-list (cdr l )))
            (cons (car l ) (flatten-list (cdr l )))
         ) 
      )
   )
)



