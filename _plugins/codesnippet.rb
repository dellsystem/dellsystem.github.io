module Jekyll
	class CodeSnippetTag < Liquid::Tag
		def initialize(tag_name, text, tokens)
			super
            @filename = text.strip
		end

		def render(context)
            file = File.join(context.registers[:site].source, 'code', @filename)
            puts file
            contents = File.read(file)
            puts contents
            return contents
		end
	end
end

Liquid::Template.register_tag('codesnippet', Jekyll::CodeSnippetTag)
