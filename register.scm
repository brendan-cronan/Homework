;Worked with Luke Basset.

;default tax rate.
(define tax_rate .065)
;intro display lines.
(newline)(display "Welcome to your cash register.")(newline)
(display "\nStart Transaction (exit with -1)\n\n")

;basic function that controls the loop.
(define (sale inVal runningTotal)
	;perpetually display the subtotal.
	(display "Current Subtotal: ")
	(display  runningTotal) (newline)
	; if statement that checks for -1.  otherwise, it keeps calling itself.  "while" loop.
	(cond
		((eq? inVal -1) ;Displays executed in reverse order for some reason. So, these are backwards from their intended output.
			((display "Goodbye!")

			(newline)(display (+ runningTotal (* runningTotal tax_rate))); add tax rate to the total.
			(display "Total: ")

			(newline) (display  (* runningTotal tax_rate)) ; multiply total by tax rate.
			(display "Tax from Subtotal: ")  
			)
		)
	)

		(display "Enter Next Value: ");Wouldn't display message when in else.
		; if it isnt -1 ...
		(else 
			(display "Enter Next Value\n")(
				(let((val (read)))( ; assign val to their input
					(if(eq? val -1) ; check for not -1
						(sale val runningTotal) ; if it is -1 then call the function without adding the val. the -1 will be caught above.
						(sale val (+ val runningTotal)) ; if it is anything other than -1, add the val to the total and call again.
					)
				))
			)  
		)
)
(sale 0 0) ;start the function for the first time.
