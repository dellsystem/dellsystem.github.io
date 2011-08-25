require 'rubygems'
require 'json'
require 'httpclient'

module Jekyll
	class ModFeaturesTag < Liquid::Tag

		def initialize(tag_name, text, tokens)
			super
            @text = text
		end

		def render(context)
            text = @text.split(" ")
			username = 'dellsystem'
			state = text[0] == 'open' ? 'open' : 'closed'
			repo_name = text[1]
			issues_url = "https://github.com/api/v2/json/issues/list/#{username}/#{repo_name}/" << state
			client = HTTPClient.new
	
			issues = JSON.parse(client.get_content(issues_url))['issues']
			
			result = ''
			issues.each {|issue|
				issue_number = issue['number']
				issue_url = issue['html_url']
				issue_body = issue['body']
				result << "*\t" << issue['title'] << " (issue [##{issue_number}](#{issue_url} \"#{issue_body}\"))" << "\n"
			}

			result
		end
	end
end

Liquid::Template.register_tag('features', Jekyll::ModFeaturesTag)
