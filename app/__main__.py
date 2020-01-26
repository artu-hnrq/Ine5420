import app.view as view
import app.domain as domain

domain.create(
	name='d',
	type='Dot',
	color=(1, 0, 0),
	coordinates=[(500, 500, 1)]
)

domain.create(
	name='t',
	type='Trace',
	color=(0, 1, 0),
	coordinates=[(50, 60, 1), (80, 100, 1)]
)

domain.create(
	name='w',
	type='Wireframe',
	color=(0, 0, 1),
	coordinates=[(100, 100, 1), (100, 400, 1), (400, 400, 1), (400, 100, 1)]
)

# domain.create(
# 	name='bzc',
# 	type='Bezier_curve',
# 	color=(1, 0, 1),
# 	coordinates=[(100, 100), (100, 400), (400, 400), (400, 100)]
# )
#
# domain.create(
# 	name='bsc',
# 	type='Bspine_curve',
# 	color=(1, 1, 1),
# 	coordinates=[(100, 100), (100, 400), (400, 400), (400, 100)]
# )

view.run()
