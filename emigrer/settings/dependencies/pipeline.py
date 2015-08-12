PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'

PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'

PIPELINE_COMPILERS = (
  'pipeline.compilers.coffee.CoffeeScriptCompiler',
  'pipeline.compilers.less.LessCompiler',
)

#GROUPS
PIPELINE_CSS = {
	'landing': {
		'source_filenames': (
			'landing/less/*.less',
		),
		'output_filename': 'landing/dist/css/style.min.css'
	}
}

PIPELINE_JS = {

}